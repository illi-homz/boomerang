from django.core.paginator import Paginator
from rest_framework import generics
from django.http import HttpResponse

from app import models
from app import serializer


class NewsList(generics.ListAPIView):
    queryset = models.New.objects.all()
    serializer_class = serializer.NewSerializer

    def get_queryset(self):
        news_on_page = 6
        page = int(self.request.GET.get('page')) or 1
        queryset = models.New.objects.all().order_by('-date')[news_on_page*(page-1):news_on_page*page]
        return queryset
