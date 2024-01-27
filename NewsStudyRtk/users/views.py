from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from news.models import Article
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import Group
from .forms import AccountUpdateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
import os

# def profile(request):
#     context = dict()
#     return render(request,'users/profile.html',context)
#
# def index(request):
#     user_acc = Account.objects.get(user=request.user)
#     context = {'user_acc': user_acc}
#     return render(request,'users/account.html', context)

def index(request):
    context = dict()
    return render(request,'users/account.html',context)

@login_required
def add_to_favorites(request, id):
    article = Article.objects.get(id=id)
    bookmark = FavoriteArticle.objects.filter(user=request.user.id, article=article)
    if bookmark.exists():
        bookmark.delete()
        status = 'removed'
        messages.warning(request, f"Новость {article.title} удалена из закладок")
    else:
        bookmark = FavoriteArticle.objects.create(user=request.user, article=article)
        status = 'added'
        messages.success(request, f"Новость {article.title} добавлена в закладки")
    response = {
        'status': status,
        'id': id,
    }
    return JsonResponse(response)

def favorites(request):
    favorites = FavoriteArticle.objects.filter(user=request.user).select_related('article')
    p = Paginator(favorites, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'users/favorites.html', {'favorites': page_obj})

def remove_favorite(request, id):
    favorite = get_object_or_404(FavoriteArticle, pk=id, user=request.user)
    favorite.delete()
    return redirect('favorites')

# def profile_update(request):
#     user = request.user
#     account = Account.objects.get(user=user)
#     if request.method == "POST":
#         user_form = UserUpdateForm(request.POST, instance=user)
#         account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)
#         if user_form.is_valid() and account_form.is_valid():
#             user_form.save()
#             account_form.save()
#             messages.success(request,"Профиль успешно обновлен")
#             return redirect('user_index')
#     else:
#         context = {'account_form':AccountUpdateForm(instance=account),
#                    'user_form':UserUpdateForm(instance=user)}
#     return render(request,'users/edit_profile.html',context)

def profile_update(request):
    user = request.user
    account = Account.objects.get(user=user)
    print(user.account.account_image)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)
        existing = account.account_image
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            # Проверяем, является ли текущее изображение равным 'default.jpg'
            if os.path.exists(existing.path) and existing.name != 'default.jpg':
                # Удаляем старое изображение
                os.remove(existing.path)

            messages.success(request, "Профиль успешно обновлен")
            return redirect('user_index')
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user)}
    return render(request,'users/edit_profile.html',context)

def password_update(request):
    user = request.user
    form = PasswordChangeForm(user,request.POST)
    if request.method == 'POST':
        if form.is_valid():
            password_info = form.save()
            update_session_auth_hash(request,password_info)
            messages.success(request,'Пароль успешно изменен')
            return redirect('user_index')

    context = {"form": form}
    return render(request,'users/edit_password.html',context)

def registration(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #появляется новый пользователь

            category = request.POST['account_type']
            if category == 'author':
                group = Group.objects.get(name='Actions Required')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='Reader')
                user.groups.add(group)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)

            login(request, user)

            # Создание объекта Account
            account = Account.objects.create(user=user)

            messages.success(request,f'{username} был зарегистрирован!')
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'users/registration.html',context)

# def contact_page(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print('Сообщение отправлено', form.cleaned_data)
#         else:
#             print(form.errors)
#     else:
#         form = ContactForm()
#         form.name='Любимый клиент'
#     context = {'form': form}
#     return render(request,'users/contact_page.html',context)

def search_auto(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term','')
        articles = Article.objects.filter(title__icontains=q)
        results =[]
        for a in articles:
            results.append(a.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено разработчикам сайта! Благодарим Вас за обратную связь!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'users/contact_page.html', {'form': form})

def my_news_list(request):
    categories = Article.categories #создали перечень категорий
    author = User.objects.get(id=request.user.id) #создали перечень авторов
    articles = Article.objects.filter(author=author)
    if request.method == "POST":
        selected_category = int(request.POST.get('category_filter'))
        if selected_category != 0: #фильтруем найденные результаты по категориям
            articles = articles.filter(category__icontains=categories[selected_category-1][0])
    else: #если страница открывется впервые
        selected_category = 0
    total = len(articles)
    p = Paginator(articles,1)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'articles': page_obj, 'total':total,
               'categories':categories,'selected_category': selected_category}

    return render(request,'users/my_news_list.html',context)

def article_favorite_btn(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'users/my_news_favorite_btn.html', context)

