from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='of'),
    path('contacts/', views.contacts, name='contact'),
    path('demoform/',views.demoform),
    path('showlastmodel/',views.showlastmodel),
    path('', views.index, name='demo'),
]
