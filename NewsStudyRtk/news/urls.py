from django.urls import path

from . import views
urlpatterns = [
    path('show/', views.index, name='news_index'),
    # path('show/<int:id>', views.detail, name='news_detail'),
    path('show/<int:pk>', views.ArticleDetailView.as_view(), name='news_detail'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='news_delete'),
    path('show/public/<int:id>', views.individual, name='user_detail'),
    path('create', views.create_article, name='create_article')
]