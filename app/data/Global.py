from django.conf import settings
static = settings.STATIC_URL

data = {
    'header': {
        'links': [
            {'title': 'о нас', 'url': '/about?tab=history'},
            {'title': 'новости', 'url': '/news'},
            {'title': 'услуги ', 'url': '/services?tab=hm'},
            {'title': 'наши цены', 'url': '#'},
            {'title': 'статьи', 'url': '#'},
            {'title': 'контакты', 'url': '#'},
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
        ]
    },
    'footer': {},

    'noManyBanner': static + 'img/index/promo/big',

    'techСharacteristic': 'Технические характеристики',
    'detail': 'Подробнее',
    'showMore': 'Показать еще'
}
