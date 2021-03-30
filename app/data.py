from django.conf import settings
static = settings.STATIC_URL

data = {
    'header': {
        'links': [
            {'title': 'о нас', 'url': '#'},
            {'title': 'новости', 'url': '#'},
            {'title': 'услуги ', 'url': '#'},
            {'title': 'наши цены', 'url': '#'},
            {'title': 'статьи', 'url': '#'},
            {'title': 'контакты', 'url': '#'},
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
        ]
    },
    'banner': {
        'title': 'Пультовая охрана <br>в Нижнем Новгороде',
        'data': [
            {'count': 27, 'text': 'лет на рынке <br>охранных предприятий'},
            {'count': 3000, 'text': 'охраняемых объектов'},
            {'count': 52, 'text': 'единицы <br>огнестрельного оружия'},
            {'count': 750, 'text': 'наш штат работников в настоящее время'},
        ]
    },
    'services': {
        'slides': [
            {
                'title': 'Охрана объектов',
                'link': {
                    'title': 'про охрану объектов',
                    'url': '#'
                },
                'img': static + 'img/slider/home'
            },
            {
                'title': 'Охрана объектов',
                'link': {
                    'title': 'про еще чего нибудь там',
                    'url': '#'
                },
                'img': static + 'img/slider/home'
            },
            {
                'title': 'Охрана объектов',
                'link': {
                    'title': 'про охрану объектов',
                    'url': '#'
                },
                'img': static + 'img/slider/home'
            },
            {
                'title': 'Охрана объектов',
                'link': {
                    'title': 'про охрану объектов',
                    'url': '#'
                },
                'img': static + 'img/slider/home'
            },
        ]
    }
}

header = {
    'header': data['header'],
    'banner': data['banner'],
    'services': data['services'],
}
