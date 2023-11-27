from django.shortcuts import render, HttpResponse
from .models import *
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
