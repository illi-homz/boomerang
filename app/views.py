from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.views.decorators.http import require_GET

import random

from . import data
from . import models

from .services.set_cookie import set_cookie
from .services.get_locale import get_locale


def index(request):
    locale = get_locale(request)
    current_data = data.Index.data[locale]
    current_data['locale'] = locale
    # print('locale',locale)

    services = models.Service.objects.all()
    currentServices = (random.sample(list(services), len(services))
                       if len(services) <= 5
                       else random.sample(list(services), 7))
    current_data['services']['slides'] = (
        currentServices if len(services) > 0 else [])

    stocks = models.Stock.objects.all()
    randomStocks = random.sample(list(stocks), 3)
    current_data['promo']['promos'] = randomStocks

    current_data['news_list'] = models.New.objects.all().order_by('-date')[:10]
    print('news_list', current_data['news_list'][0].date)
    response = HttpResponse(render(request, 'Index.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def about(request):
    tab = request.GET.get('tab')
    if (not bool(tab)):
        return redirect('/about?tab=history')
    locale = get_locale(request)
    current_data = data.About.data[locale]
    current_data['locale'] = locale
    current_data['tab'] = tab
    current_data['galery'] = models.Photo.objects.all()
    current_data['clients'] = models.Client.objects.all()
    current_data['feedbacks'] = models.Feedback.objects.all()
    response = HttpResponse(render(request, 'About.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def news(request):
    locale = get_locale(request)
    current_data = data.News.data[locale]
    current_data['locale'] = locale
    current_data['news'] = models.New.objects.all().order_by('-date')[:6]
    response = HttpResponse(render(request, 'News.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def news_item(request, pk):
    locale = get_locale(request)
    current_data = data.NewsDetail.data[locale]
    current_data['locale'] = locale
    new = models.New.objects.get(id=pk)
    current_data['new'] = new
    news = models.New.objects.all().order_by('-date')
    current_data['news'] = [n for n in news if n.id != pk][:6]
    current_data['breadCrumbs'][-1]['title'] = new.title()[locale]
    response = HttpResponse(render(request, 'NewsDetail.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def services(request):
    tab = request.GET.get('tab')
    if (not bool(tab)):
        return redirect('/services?tab=hm')
    locale = get_locale(request)
    current_data = data.Services.data[locale]
    current_data['locale'] = locale
    current_data['tab'] = tab
    current_data['services'] = models.Service.objects.filter(type=tab)
    response = HttpResponse(render(request, 'Services.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def services_item(request, pk):
    locale = get_locale(request)
    current_data = data.ServicesDetail.data[locale]
    current_data['locale'] = locale
    service = models.Service.objects.get(id=pk)
    current_data['serviceItem'] = service
    services = models.Service.objects.all()
    current_data['services'] = random.sample(list(services), 6) if len(
        services) >= 6 else random.sample(list(services), len(services))
    current_data['breadCrumbs'][-1]['title'] = service.title()[locale]
    response = HttpResponse(
        render(request, 'ServicesDetail.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def stocks(request):
    locale = get_locale(request)
    current_data = data.Stocks.data[locale]
    current_data['locale'] = locale
    current_data['stocks'] = models.Stock.objects.all()
    response = HttpResponse(render(request, 'Stocks.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def articles(request):
    locale = get_locale(request)
    current_data = data.Articles.data[locale]
    current_data['locale'] = locale
    arts = models.Article.objects.all()
    current_data['articles'] = [
        {'id': a.id, 'title': a.title, 'category': a.category} for a in arts]
    current_data['categories'] = models.article_categoryes[locale]
    response = HttpResponse(render(request, 'Articles.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def article_item(request, pk):
    locale = get_locale(request)
    current_data = data.ArticleDetail.data[locale]
    current_data['locale'] = locale
    article = models.Article.objects.get(id=pk)
    current_data['article'] = article
    current_data['breadCrumbs'][-1]['title'] = article.title()[locale]
    response = HttpResponse(
        render(request, 'ArticleDetail.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def contacts(request):
    locale = get_locale(request)
    current_data = data.Contacts.data[locale]
    current_data['locale'] = locale
    response = HttpResponse(render(request, 'Contacts.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def documents(request):
    locale = get_locale(request)
    current_data = data.Documents.data[locale]
    current_data['locale'] = locale
    current_data['documents'] = models.Document.objects.all()
    response = HttpResponse(render(request, 'Documents.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def site_map(request):
    locale = get_locale(request)
    current_data = data.SiteMap.data[locale]
    current_data['locale'] = locale
    response = HttpResponse(render(request, 'SiteMap.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def links(request):
    locale = get_locale(request)
    current_data = data.Links.data[locale]
    current_data['links'] = models.Link.objects.all()
    current_data['locale'] = locale
    response = HttpResponse(render(request, 'Links.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


def handle_page_not_found(request, exception):
    # def handle_page_not_found(request):
    locale = get_locale(request)
    current_data = data.Page404.data[locale]
    current_data['locale'] = locale
    response = HttpResponse(render(request, 'Page404.jinja', current_data))
    response = set_cookie(response, 'locale', locale)
    return response


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Crawl-delay: 5",
        "Host: bumaranger.ru",
        "Disallow: /my-admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
