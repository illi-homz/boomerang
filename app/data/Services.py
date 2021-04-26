from django.conf import settings
static = settings.STATIC_URL

data = {
    'RU': {
        'title': 'Услуги',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Услуги', 'url': '#'}
        ],

        'linksList': [
            {'title': 'Oхранные услуги', 'url': '/services?tab=hm', 'tab': 'hm'},
            {'title': 'Техническая охрана', 'url': '/services?tab=th', 'tab': 'th'},
            {'title': 'Изготовление спецодежды', 'url': '/services?tab=ds', 'tab': 'ds'},
            {'title': 'Консультационные и юридические услуги', 'url': '/services?tab=cs', 'tab': 'cs'}
        ],
    },
    'EN': {
        'title': 'Услуги',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Услуги', 'url': '#'}
        ],

        'linksList': [
            {'title': 'Oхранные услуги', 'url': '/services?tab=hm', 'tab': 'hm'},
            {'title': 'Техническая охрана', 'url': '/services?tab=th', 'tab': 'th'},
            {'title': 'Изготовление спецодежды', 'url': '/services?tab=ds', 'tab': 'ds'},
            {'title': 'Консультационные и юридические услуги', 'url': '/services?tab=cs', 'tab': 'cs'}
        ],
    }
}
