from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count, Avg, Max
#from django.views.decorators.cache import cache_page
from .models import *
from django.db import connection, reset_queries
from users.models import Account
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url="/")
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None: #проверили что не аноним
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save() #сохраняем в БД
                form = ArticleForm()
                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request,'news/create_article.html', {'form':form})

#@cache_page(60 * 1)
def index(request):
    #today_articles = Article.published.all()
    # context = {'today_articles': articles}

    author_list = User.objects.all()
    selected = 0
    if request.method == "POST":
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            articles = Article.objects.all()
        elif selected == 1000:
            articles = Article.published.all()
        else:
            articles = Article.objects.filter(author=selected)
    else:
        articles = Article.objects.all()
    context = {'articles': articles, 'author_list': author_list, 'selected': selected}
    return render(request, 'news/news.html', context)

#@cache_page(60 * 1)
def detail(request, id):
    nick = Account.objects.all().values_list('nickname', flat=True).filter(article=id)[0]
    print(nick)

    article = Article.objects.select_related('author').filter(id=id)[0]
    context = {'article': article, 'nick': nick}
    return render(request, 'news/details.html', context)
#@cache_page(60 * 1)
def individual(request,id):
    author = Account.objects.filter(user_id=id)[0]
    context = {'author': author}
    return render(request, 'users/public_page.html', context)
