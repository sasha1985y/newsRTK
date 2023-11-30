from django.shortcuts import render, HttpResponse
from .models import *
from django.db import connection, reset_queries
from users.models import Account
def index(request):
    author_list = User.objects.all()
    selected = 0
    if request.method == "POST":
        print(request.POST)
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected)
        print('connection.queries :', connection.queries)
    else:
        articles = Article.objects.all()
    context = {'articles': articles, 'author_list': author_list, 'selected': selected}
    return render(request, 'news/news.html', context)


def detail(request, id):
    article = Article.objects.filter(id=id)[0]
    context = {'article': article}
    return render(request, 'news/details.html', context)

def individual(request,id):
    author = Account.objects.filter(user_id=id)[0]
    context = {'author': author}
    return render(request, 'users/public_page.html', context)
