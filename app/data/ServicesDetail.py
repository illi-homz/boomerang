from django.conf import settings
static = settings.STATIC_URL
from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Услуги', 'url': '/services'},
            {'title': 'Услуги', 'url': '#'}
        ],
    },
    'EN': {
        **global_data['EN'],
        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Services', 'url': '/services'},
            {'title': 'Services', 'url': '#'}
        ],
    }
}
