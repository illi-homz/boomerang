from django.conf import settings
static = settings.STATIC_URL
import datetime

currentYear = datetime.date.today().year

data = {
    'RU': {
        'titleDesc': 'ЧОП Бумеранг - пультовая охрана, тревожная кнопка, техническая охрана, охрана персонала и материальных ценностей, сопровождение грузов по территории РФ, охранное предприятие ',
        'lightTheme': 'Светлая тема',
        'lightSiteTheme': 'Светлая тема сайта',
        'darkTheme': 'Темная тема',
        'darkSiteTheme': 'Темная тема сайта',
        'header': {
            'links': [
                {'title': 'о нас', 'url': '/about?tab=history'},
                {'title': 'услуги ', 'url': '/services?tab=hm'},
                {'title': 'акции', 'url': '/stocks'},
                {'title': 'новости', 'url': '/news'},
                {'title': 'статьи', 'url': '/articles'},
                {'title': 'контакты', 'url': '/contacts'},
                {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
            ]
        },
        'footer': {
            'toUp':         {'title': 'Наверх', 'url': '#header'},
            'services':     {'title': 'Услуги', 'url': '/services?tab=hm'},
            'ourPrices':    {'title': 'Акции', 'url': '/stocks'},
            'news':         {'title': 'Новости', 'url': '/news'},
            'aboutUs':      {'title': 'О нас', 'url': '/about?tab=history'},
            'articles':     {'title': 'Статьи', 'url': '/articles'},
            'contacts':     {'title': 'Контакты', 'url': '/contacts'},
            'chop':         {'title': f'© 2006‐{currentYear} ЧОП «Бумеранг»', 'url': ''},
            'siteMap':      {'title': 'Карта сайта', 'url': '/site-map'},
            'links':        {'title': 'Полезные ссылки', 'url': '/links'},
            'docs':         {'title': 'Документы', 'url': '/documents'}
        },
        'footerContacts': [
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7 (831) 28-28-911'},
            {'title': '+7 (953) 571-88-77', 'url': 'tel:+7 (953) 571-88-77'},
            {'title': '+7 (951) 910-10-03', 'url': 'tel:+7 (951) 910-10-03'},
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
        'lightTheme': 'Light theme',
        'lightSiteTheme': 'Light site theme',
        'darkTheme': 'Dark theme',
        'darkSiteTheme': 'Black site theme',
        'header': {
            'links': [
                {'title': 'about us', 'url': '/about?tab=history'},
                {'title': 'services ', 'url': '/services?tab=hm'},
                {'title': 'stocks', 'url': '/stocks'},
                {'title': 'news', 'url': '/news'},
                {'title': 'articles', 'url': '/articles'},
                {'title': 'contacts', 'url': '/contacts'},
                {'title': '+7 (831) 28-28-911', 'url': 'tel:+7(831)28-28-911'},
            ]
        },
        'footer': {
            'toUp':         {'title': 'Up', 'url': '#header'},
            'services':     {'title': 'Services', 'url': '/services?tab=hm'},
            'ourPrices':    {'title': 'Stocks', 'url': '/stocks'},
            'news':         {'title': 'News', 'url': '/news'},
            'aboutUs':      {'title': 'About us', 'url': '/about?tab=history'},
            'articles':     {'title': 'Articles', 'url': '/articles'},
            'contacts':     {'title': 'Contacts', 'url': '/contacts'},
            'chop':         {'title': f'© 2006‐{currentYear} PSC «Boomerang»', 'url': ''},
            'siteMap':      {'title': 'Site map', 'url': '/site-map'},
            'links':        {'title': 'Links', 'url': '/links'},
            'docs':         {'title': 'Documents', 'url': '/documents'}
        },
        'footerContacts': [
            {'title': '+7 (831) 28-28-911', 'url': 'tel:+7 (831) 28-28-911'},
            {'title': '+7 (953) 571-88-77', 'url': 'tel:+7 (953) 571-88-77'},
            {'title': 'bumerang52@list.ru', 'url': 'mailto:bumerang52@list.ru'},
            {'title': 'We are on VKontakte', 'url': 'https://vk.com/52bumerang52'},
        ],
        'noManyBanner': static + 'img/index/promo/big',
        'noManyInstall': 'Free equipment installation',
        'rentTerms': 'On lease terms',

        'techСharacteristic': 'Specifications',
        'detail': 'Detail',
        'showMore': 'Show more',
        'seeSame': 'See also',
        'readSame': 'Read also',
        'moreDetails': 'More details',
    },
}
