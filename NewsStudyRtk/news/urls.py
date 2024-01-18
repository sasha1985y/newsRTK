from django.urls import path

from . import views
urlpatterns = [
    path('show/', views.index, name='news_index'),
    path('show/search_auto/', views.search_auto, name='search_auto'),
    path('show/<int:pk>', views.ArticleDetailView.as_view(), name='news_detail'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='news_update'),
    path('update_cover/<int:pk>', views.ArticleUpdateCover.as_view(), name='news_update_cover'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='news_delete'),
    path('show/public/<int:id>', views.individual, name='user_detail'),
    path('create', views.create_article, name='create_article'),
    path('news_request/', views.news_request, name='news_request'),
    path('news_input/', views.news_input, name='news_input'),
    path('show/readers', views.readers, name='news_readers'),
    path('readers/public/<int:id>', views.individual, name='user_detail'),
    path('news_subscribe/', views.news_subscribe, name='news_subscribe'),
]