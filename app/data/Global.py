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
        # },
        'footer': {
            'toUp':         {'title': 'Наверх', 'url': '#header'},
            'services':     {'title': 'Услуги', 'url': '/services?tab=hm'},
            'ourPrices':    {'title': 'Наши цены', 'url': '/prices'},
            'news':         {'title': 'Новости', 'url': '/news'},
            'aboutUs':      {'title': 'О нас', 'url': '/about?tab=history'},
            'articles':     {'title': 'Статьи', 'url': '/articles'},
            'contacts':     {'title': 'Контакты', 'url': '/contacts'},
            'chop':         {'title': 'ЧОП «Бумеранг»', 'url': ''},
            'siteMap':      {'title': 'Карта сайта', 'url': '/site-map'},
            'links':        {'title': 'Полезные ссылки', 'url': '/links'},
            'docs':         {'title': 'Документы', 'url': '/documents'}
        },
        'footerContacts': [
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7 (831) 28-28-911'},
            {'title': '28-26-112', 'url': 'tel:28-26-112'},
            {'title': '28-26-110', 'url': 'tel:28-26-110'},
            {'title': 'bumerang52@list.ru', 'url': 'mailto:bumerang52@list.ru'},
            {'title': 'Мы ВКонтакте', 'url': 'https://vk.com/52bumerang52'},
        ],
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
            'toUp':         {'title': 'Up', 'url': '#header'},
            'services':     {'title': 'Services', 'url': '/services?tab=hm'},
            'ourPrices':    {'title': 'Our prices', 'url': '/prices'},
            'news':         {'title': 'News', 'url': '/news'},
            'aboutUs':      {'title': 'About us', 'url': '/about?tab=history'},
            'articles':     {'title': 'Articles', 'url': '/articles'},
            'contacts':     {'title': 'Contacts', 'url': '/contacts'},
            'chop':         {'title': 'PSC «Boomerang»', 'url': ''},
            'siteMap':      {'title': 'Site map', 'url': '/site-map'},
            'links':        {'title': 'Links', 'url': '/links'},
            'docs':         {'title': 'Documents', 'url': '/documents'}
        },
        'footerContacts': [
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7 (831) 28-28-911'},
            {'title': '28-26-112', 'url': 'tel:28-26-112'},
            {'title': '28-26-110', 'url': 'tel:28-26-110'},
            {'title': 'bumerang52@list.ru', 'url': 'mailto:bumerang52@list.ru'},
            {'title': 'We are on VKontakte', 'url': 'https://vk.com/52bumerang52'},
        ],
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
