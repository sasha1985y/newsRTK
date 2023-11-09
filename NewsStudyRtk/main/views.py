from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News

def index(request):
    value = -10
    n1 = News('Новость 1','Текст 1','07.11.23')
    n2 = News('Новость 2','Текст 2','01.11.23')
    l = [n1, n2]
    d = { 1: 'один', 'Два': 2}

    context = {'title': 'Страница главная',
               'Header1': 'Заголовок страницы',
               'numbers': l,
               'dictionary': d
               }
    context['пример']= 'Example'
    return render(request,'main/index.html', context)


def about(request):
    return HttpResponse('<h1> о нас </h1>')


def contacts(request):
    return HttpResponse('<h1> контакты </h1>')


def sidebar(request):
    return render(request,'main/sidebar.html')

def header(request):
    return render(request,'main/header.html')

def foot(request):
    return render(request,'main/foot.html')