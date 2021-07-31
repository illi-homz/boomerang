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
    path('stocks', views.stocks),
    path('articles', views.articles),
    path('articles/<int:pk>', views.article_item),
    path('contacts', views.contacts),
    path('documents', views.documents),
    path('site-map', views.site_map),
    path('links', views.links),
    # path('404', views.handle_page_not_found),

    path('api/get-news', NewsList.as_view(), name='news-list'),

    path("robots.txt", views.robots_txt),
]
