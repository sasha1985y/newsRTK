from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('private/', views.index, name='user_index'),
    path('private/update', views.profile_update, name='profile_update'),
    path('contact_page', views.contact_page, name='contact_page'),
    path('registration',views.registration,name='registration'),
    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password', views.password_update, name='password'),
    path('favorites/<int:id>', views.add_to_favorites, name='favorites'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/<int:id>/remove/', views.remove_favorite, name='remove_favorite'),
    path('mynewslist',views.my_news_list,name='my_news_list'),
]
