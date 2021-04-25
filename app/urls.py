from django.urls import path, include

from . import views
from .services.news import NewsList


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('news', views.news),
    path('news/<int:pk>', views.news_item),
    path('services', views.services),
    path('services/<int:pk>', views.services_item),
    path('prices', views.prices),
    path('articles', views.articles),
    path('articles/<int:pk>', views.article_item),
    path('contacts', views.contacts),
    path('documents', views.documents),

    path('api/get-news', NewsList.as_view(), name='news-list'),

    # path('404', views.page_not_found_view),
]
