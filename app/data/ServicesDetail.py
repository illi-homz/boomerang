from django.conf import settings
static = settings.STATIC_URL

data = {
    'RU': {
        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Услуги', 'url': '/services'},
            {'title': 'Услуги', 'url': '#'}
        ],
    },
    'RU': {
        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Services', 'url': '/services'},
            {'title': 'Services', 'url': '#'}
        ],
    }
}
