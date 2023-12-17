from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count, Avg, Max
#from django.views.decorators.cache import cache_page
from .models import *
from django.db import connection, reset_queries
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView
from users.models import Account
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import *
import json


#URL:    path('search_auto/', views.search_auto, name='search_auto'),
def search_auto(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term','')
        articles = Article.objects.filter(title__icontains=q)
        results =[]
        for a in articles:
            results.append(a.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

@login_required(login_url=settings.LOGIN_URL)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None: #проверили что не аноним
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.account_id = current_user.id
                new_article.save() #сохраняем в БД
                form.save_m2m()
                for img in request.FILES.getlist('image_field'):
                    Image.objects.create(article=new_article, image=img, title=img.name)
                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request,'news/create_article.html', {'form':form})

def index(request):
    #categories = Article.objects.all().values_list('category', flat=True)
    categories = Article.categories
    author_list = User.objects.all()
    selected = 0
    if request.method == "POST":
        selected = int(request.POST.get('author_filter'))
        selected_category = int(request.POST.get('category_filter'))
        if selected == 0:
            articles = Article.objects.all()
        elif selected == 1000:
            articles = Article.published.all()
        else:
            articles = Article.objects.filter(author=selected)
        if selected_category != 0:  # фильтруем найденные по авторам результаты по категориям
            articles = articles.filter(category__icontains=categories[selected_category - 1][0])
    else:
        selected_category = 0
        articles = Article.objects.all()
    context = {'articles': articles, 'author_list': author_list, 'selected': selected, 'categories':categories,'selected_category': selected_category}
    return render(request, 'news/news.html', context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object = self.object
        images = Image.objects.filter(article=current_object)
        context['images'] = images
        return context

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news/create_article.html'
    fields = ['title','anouncement','text','tags','category']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news_index') #именованная ссылка или абсолютную
    template_name = 'news/delete_article.html'

#@login_required(login_url=settings.LOGIN_URL)
def individual(request,id):
    author = Account.objects.filter(user_id=id)[0]
    context = {'author': author}
    return render(request, 'users/public_page.html', context)
