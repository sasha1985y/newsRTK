from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from .models import News
# from .models import Link

'''def index(request):
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
    return render(request,'main/index.html', context)'''

# def sidebar(request):
#     home = Link('<li><i class="fa-solid fa-house"></i><a href="/" style="text-decoration: none; color: #FDCE4B;">&nbspДомой</a></li>')
#     context = {
#         'home': home
#     }
#     return render(request, 'main/sidebar.html', context)


def about(request):
    return render(request,'main/about.html')

def index(request):
    return render(request,'main/index.html')

def contacts(request):
    return render(request,'main/contacts.html')

def news(request):
    return render(request,'main/news.html')

def account(request):
    return render(request,'main/account.html')
