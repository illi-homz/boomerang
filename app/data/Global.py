from django.conf import settings
static = settings.STATIC_URL

data = {
    'RU': {
        'titleDesc': 'ЧОП Бумеранг - пультовая охрана, тревожная кнопка, техническая охрана, храна персонала и материальных ценностей, сопровождение грузов по территории РФ, охранное предприятие ',
        'header': {
            'links': [
                {'title': 'о нас', 'url': '/about?tab=history'},
                {'title': 'новости', 'url': '/news'},
                {'title': 'услуги ', 'url': '/services?tab=hm'},
                {'title': 'наши цены', 'url': '/prices'},
                {'title': 'статьи', 'url': '/articles'},
                {'title': 'контакты', 'url': '/contacts'},
                {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
            ]
        },
        'footer': {
            'toUp': 'Наверх',
            'services': 'Услуги',
            'ourPrices': 'Наши цены',
            'news': 'Новости',
            'aboutUs': 'О нас',
            'articles': 'Статьи',
            'contacts': 'Контакты',
            'chop': 'ЧОП «Бумеранг»',
            'siteMap': 'Карта сайта',
            'links': 'Полезные ссылки',
            'docs': 'Документы',
        },
        'noManyBanner': static + 'img/index/promo/big',
        'noManyInstall': 'Бесплатная установка оборудования',
        'rentTerms': 'На условиях аренды',

        'techСharacteristic': 'Технические характеристики',
        'detail': 'Подробнее',
        'showMore': 'Показать еще',
        'seeSame': 'Смотрите так же',
        'readSame': 'Читайте так же',
        'moreDetails': 'Подробнее'
    },
    'EN': {
        'titleDesc': 'PSC Boomerang - monitored security system, alarm button, technical security, security of personnel and material values, escort of goods on the territory of the Russian Federation, security company',
        'header': {
            'links': [
                {'title': 'about us', 'url': '/about?tab=history'},
                {'title': 'news', 'url': '/news'},
                {'title': 'services ', 'url': '/services?tab=hm'},
                {'title': 'our prices', 'url': '/prices'},
                {'title': 'articles', 'url': '/articles'},
                {'title': 'contacts', 'url': '/contacts'},
                {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
            ]
        },
        'footer': {
            'toUp': 'Up',
            'services': 'Services',
            'ourPrices': 'Our prices',
            'news': 'News',
            'aboutUs': 'About us',
            'articles': 'Articles',
            'contacts': 'Contacts',
            'chop': 'PSC Boomerang',
            'siteMap': 'Site map',
            'links': 'Links',
            'docs': 'Documents',
        },
        'noManyBanner': static + 'img/index/promo/big',
        'noManyInstall': 'No money install',
        'rentTerms': 'Rent terms',

        'techСharacteristic': 'Specifications',
        'detail': 'Detail',
        'showMore': 'Show more',
        'seeSame': 'See same',
        'readSame': 'Read same',
        'moreDetails': 'More details',
    },
}
