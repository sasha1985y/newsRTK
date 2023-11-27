from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

# def index(request):
#     return render(request,'news/news.html')

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'news/news.html',context)

def detail(request,id):
    article = Article.objects.filter(id=id)[0]
    context = {'article': article}
    return render(request, 'news/details.html', context)
#     #пример создания новости
#     # author = User.objects.get(id=request.user.id)
#     # article = Article(author=author,title='Заголовок1',
#     #                   anouncement='Анонс', text='текст')
#     # article.save()
#
#     #пример итерирования по объектам QuerySet
#     articles = Article.objects.all()
#     s=''
#     for article in articles:
#         s+=f'<h1>{article.title}</h1><br>'
#     return HttpResponse(s)
def individual(request,id):
    article = Article.objects.filter(id=id)[0]
    context = {'article': article}
    return render(request, 'news/public_page.html', context)
