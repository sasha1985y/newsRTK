from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data)
        else:
            print(form.errors)
    else:
        form = ContactForm()
        form.name='Любимый клиент'
    context = {'form': form}
    return render(request,'users/contact_page.html',context)

def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc.birthdate, user_acc.gender)
    context = {'user_acc': user_acc}
    return render(request,'users/account.html', context)

# def index(request):
#     print(request.user,request.user.id)
#     user_acc = Account.objects.get(user=request.user)
#     print(user_acc.birthdate, user_acc.gender)
#     return HttpResponse('Приложение Users')
