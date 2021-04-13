from django.conf import settings
static = settings.STATIC_URL

data = {
    'title': 'новости',
    'breadCrumbs': [
        {'title': 'Главная', 'url': '/'},
        {'title': 'Новости', 'url': '#'}
    ],
}
