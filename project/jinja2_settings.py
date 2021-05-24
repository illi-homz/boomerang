from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

# from jinja2 import Environment
import jinja2

def environment(**options):
    env = jinja2.Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    # env.loader = jinja2.PackageLoader('templates')
    return env
