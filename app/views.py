from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .data import Index

def index(request):
    template = loader.get_template('Index.jinja')
    return HttpResponse(template.render(Index.data))
