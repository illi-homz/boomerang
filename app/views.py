from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect

import random

from . import data
from . import models

from .services.set_cookie import set_cookie
from .services.get_locale import get_locale


g_data = data.Global.data


def index(request):
    locale = get_locale(request)
    services = models.Service.objects.all()
    current_data = data.Index.data[locale]
    current_data['locale'] = locale
    if len(services) > 0:
        mainService = services[0]
        randomServices = random.sample(list(services)[0:], 5)
        current_data['services']['slides'] = [mainService] + randomServices
    else:
        current_data['services']['slides'] = []
    current_data['news'] = models.New.objects.all().order_by('-date')[:10]
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'Index.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def about(request):
    tab =  request.GET.get('tab')
    if (not bool(tab)):
        return redirect('/about?tab=history')
    locale = get_locale(request)
    current_data = data.About.data[locale]
    current_data['locale'] = locale
    current_data['tab'] = tab
    current_data['galery'] = models.Photo.objects.all()
    current_data['clients'] = models.Client.objects.all()
    current_data['feedbacks'] = models.Feedback.objects.all()
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'About.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def news(request):
    locale = get_locale(request)
    current_data = data.News.data[locale]
    current_data['locale'] = locale
    current_data['news'] = models.New.objects.all().order_by('-date')[:6]
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'News.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def news_item(request, pk):
    locale = get_locale(request)
    current_data = data.NewsDetail.data[locale]
    current_data['locale'] = locale
    new = models.New.objects.get(id = pk)
    current_data['new'] = new
    current_data['news'] = models.New.objects.all().order_by('-date')[:6]
    current_data['breadCrumbs'][-1]['title'] = new.title()[locale]
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'NewsDetail.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def services(request):
    tab =  request.GET.get('tab')
    if (not bool(tab)):
        return redirect('/services?tab=hm')
    locale = get_locale(request)
    current_data = data.Services.data[locale]
    current_data['locale'] = locale
    current_data['tab'] = tab
    current_data['services'] = models.Service.objects.filter(type = tab)
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'Services.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def services_item(request, pk):
    locale = get_locale(request)
    current_data = data.ServicesDetail.data[locale]
    current_data['locale'] = locale
    service = models.Service.objects.get(id = pk)
    current_data['serviceItem'] = service
    current_data['services'] = random.sample(list(models.Service.objects.all()), 6)
    current_data['breadCrumbs'][-1]['title'] = service.title()[locale]
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'ServicesDetail.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def prices(request):
    locale = get_locale(request)
    current_data = data.Prices.data[locale]
    current_data['locale'] = locale
    current_data['prices'] = models.Price.objects.all()
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'Prices.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def articles(request):
    locale = get_locale(request)
    current_data = data.Articles.data[locale]
    current_data['locale'] = locale
    arts = models.Article.objects.all()
    current_data['articles'] = [{'id': a.id, 'title': a.title, 'category': a.category} for a in arts]
    current_data['categories'] = models.article_categoryes[locale]
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'Articles.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def article_item(request, pk):
    locale = get_locale(request)
    current_data = data.ArticleDetail.data[locale]
    current_data['locale'] = locale
    article = models.Article.objects.get(id = pk)
    current_data['article'] = article
    current_data['breadCrumbs'][-1]['title'] = article.title()[locale]
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'ArticleDetail.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def contacts(request):
    locale = get_locale(request)
    current_data = data.Contacts.data[locale]
    current_data['locale'] = locale
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'Contacts.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

def documents(request):
    locale = get_locale(request)
    current_data = data.Documents.data[locale]
    current_data['locale'] = locale
    current_data['documents'] = models.Document.objects.all()
    current_data.update(g_data[locale])
    response = HttpResponse(render(request, 'Documents.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response

# def page_not_found_view(request):
    # return render(request,'myapp/404.html')
    # return HttpResponse('404')

def handler404(request, *args, **argv):
    return HttpResponse('404')