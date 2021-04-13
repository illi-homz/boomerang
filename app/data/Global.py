from django.conf import settings
static = settings.STATIC_URL

data = {
    'header': {
        'links': [
            {'title': 'о нас', 'url': '/about?tab=history'},
            {'title': 'новости', 'url': '/news'},
            {'title': 'услуги ', 'url': '#'},
            {'title': 'наши цены', 'url': '#'},
            {'title': 'статьи', 'url': '#'},
            {'title': 'контакты', 'url': '#'},
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
        ]
    },
    'footer': {},
    'linksList': [
        {'title': 'История', 'url': '/about?tab=history', 'tab': 'history'},
        {'title': 'Наш арсенал', 'url': '/about?tab=arsenal', 'tab': 'arsenal'},
        {'title': 'Наши клиенты', 'url': '/about?tab=clients', 'tab': 'clients'},
        {'title': 'Отзывы', 'url': '/about?tab=feedbacks', 'tab': 'feedbacks'},
        {'title': 'Вакансии', 'url': '/about?tab=vacancies', 'tab': 'vacancies'},
        {'title': 'Галерея', 'url': '/about?tab=galery', 'tab': 'galery'},
    ],
    'noManyBanner': static + 'img/index/promo/big',

    'techСharacteristic': 'Технические характеристики',
    'detail': 'Подробнее',
    'showMore': 'Показать еще'
}
