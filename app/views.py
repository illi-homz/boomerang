from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator

from . import data
from . import models


def index(request):
    data.Index.data['news'] = models.New.objects.all()[:10]
    data.Index.data.update(data.Global.data)
    return render(request, 'Index.jinja', data.Index.data)

def about(request):
    data.About.data['tab'] = request.GET.get('tab')
    data.About.data.update(data.Global.data)
    return render(request, 'About.jinja', data.About.data)

def news(request):
    data.News.data['news'] = models.New.objects.all().order_by('-date')[:6]
    data.News.data.update(data.Global.data)
    return render(request, 'News.jinja', data.News.data)

def news_item(request, pk):
    data.News.data['new'] = models.New.objects.get(id = pk)
    return render(request, 'NewsDetail.jinja', data.News.data)


def test(request):
    return render(request, 'Test.html')
