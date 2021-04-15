from django.urls import path, include

from . import views
from .services.news import NewsList

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('news', views.news),
    path('news/<int:pk>', views.news_item),
    path('services', views.services),

    path('api/get-news', NewsList.as_view(), name='news-list'),

    path('test', views.test),
]
