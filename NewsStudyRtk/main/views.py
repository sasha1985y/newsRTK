from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {'title': 'test page',
               'Header1': 'Заголовок 1'}
    return render(request, 'main/index.html', context)
def about(request):
    return HttpResponse('<h1 style="color: blue" > О нас </h1>')
def contacts(request):
    return HttpResponse('<h1 style="color: magenta" > Контакты </h1>')