from django.conf import settings
static = settings.STATIC_URL
from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],
        'title': 'Услуги',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Услуги', 'url': '#'}
        ],

        'linksList': [
            {'title': 'Oхранные услуги', 'url': '/services?tab=hm', 'tab': 'hm'},
            {'title': 'Техническая охрана', 'url': '/services?tab=th', 'tab': 'th'},
            # {'title': 'Изготовление спецодежды', 'url': '/services?tab=ds', 'tab': 'ds'},
            {'title': 'Консультационные и юридические услуги', 'url': '/services?tab=cs', 'tab': 'cs'}
        ],
    },
    'EN': {
        **global_data['EN'],
        'title': 'Services',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Services', 'url': '#'}
        ],

        'linksList': [
            {'title': 'Security services', 'url': '/services?tab=hm', 'tab': 'hm'},
            {'title': 'Technical security', 'url': '/services?tab=th', 'tab': 'th'},
            # {'title': 'Making workwear', 'url': '/services?tab=ds', 'tab': 'ds'},
            {'title': 'Consulting and legal services', 'url': '/services?tab=cs', 'tab': 'cs'}
        ],
    }
}
