from django.shortcuts import render, HttpResponse
from .models import *
from django.db import connection, reset_queries
def index(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    author_list = User.objects.all()
    selected = 0
    if request.method == "POST":
        print(request.POST)
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected)
        print(connection.queries)
    else:
        articles = Article.objects.all()
    context = {'articles': articles, 'author_list': author_list, 'selected': selected}
    return render(request, 'news/news.html', context)


def detail(request, id):
    article = Article.objects.filter(id=id)[0]
    context = {'article': article}
    return render(request, 'news/details.html', context)

def individual(request,id):
    article = Article.objects.filter(id=id)
    context = {'article': article}
    return render(request, 'news/public_page.html', context)
