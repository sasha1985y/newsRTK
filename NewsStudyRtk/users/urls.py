from django.urls import path

from . import views

urlpatterns = [
    path('private/', views.index, name='user_index'),
]
