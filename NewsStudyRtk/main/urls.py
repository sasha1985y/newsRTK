from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='of'),
    path('contacts/', views.contacts, name='contact'),
    path('news/', views.news, name='new'),
    path('account/', views.account, name='user'),
]
