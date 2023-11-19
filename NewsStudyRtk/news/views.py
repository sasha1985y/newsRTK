from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,'news/news.html')

def detail(request):
    return render(request,'news/news.html')

# def index(request):
#     article = Article.objects.all().first()
#     context = {'article':article}
#     return render(request,'news/news.html',context)
#
# def detail(request,id):
#     # article = Article.objects.filter(id=id)[0]
#     # print(article,type(article))
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
