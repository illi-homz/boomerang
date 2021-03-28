from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .data import data as main_data

def index(request):
    template = loader.get_template('Index.jinja')
    data = {
        'header': main_data['header'],
        'banner': main_data['banner']
    }
    return HttpResponse(template.render(data))
