from django.urls import path

from . import views

urlpatterns = [
    path('private/', views.index, name='user_index'),
    path('contact_page',views.contact_page,name='contact_page'),
]
