from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect

from . import data
from . import models


def index(request):
    data.Index.data['news'] = models.New.objects.all()[:10]
    data.Index.data.update(data.Global.data)
    return render(request, 'Index.jinja', data.Index.data)

def about(request):
    tab =  request.GET.get('tab')
    if (not bool(tab)):
        return redirect('/about?tab=history')
    data.About.data['tab'] = tab
    data.About.data.update(data.Global.data)
    return render(request, 'About.jinja', data.About.data)

def news(request):
    data.News.data['news'] = models.New.objects.all().order_by('-date')[:6]
    data.News.data.update(data.Global.data)
    return render(request, 'News.jinja', data.News.data)

def news_item(request, pk):
    data.NewsDetail.data['new'] = models.New.objects.get(id = pk)
    data.NewsDetail.data['news'] = models.New.objects.all().order_by('-date')[:6]
    data.NewsDetail.data['breadCrumbs'][-1]['title'] = data.NewsDetail.data['new'].desc
    return render(request, 'NewsDetail.jinja', data.NewsDetail.data)

def services(request):
    tab =  request.GET.get('tab')
    if (not bool(tab)):
        return redirect('/services?tab=hm')
    data.Services.data['tab'] = tab
    data.Services.data['services'] = models.Service.objects.filter(type = tab)
    data.Services.data.update(data.Global.data)
    return render(request, 'Services.jinja', data.Services.data)


def test(request):
    return render(request, 'Test.html')
