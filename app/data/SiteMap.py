from app.models import Service, Article
from .Global import data as global_data


services = Service.objects.all()
articles = Article.objects.all()

data = {
    'RU': {
        **global_data['RU'],
        'title': 'Карта сайта',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Карты сайта', 'url': '#'}
        ],

        'linksList': [
            { 'title': 'Главная', 'url': '/' },
            {
                'title': 'О нас',
                'url': '/about',
                'tabs': [
                    {'title': 'История', 'url': '/about?tab=history'},
                    {'title': 'Наш арсенал', 'url': '/about?tab=arsenal'},
                    {'title': 'Наши клиенты', 'url': '/about?tab=clients'},
                    {'title': 'Отзывы', 'url': '/about?tab=feedbacks'},
                    {'title': 'Вакансии', 'url': '/about?tab=vacancies'},
                    {'title': 'Галерея', 'url': '/about?tab=galery'},
                ]
            },
            { 'title': 'Новости', 'url': '/news' },
            {
                'title': 'Услуги',
                'url': '/services',
                'tabs': [
                    {
                        'title': 'Oхранные услуги',
                        'url': '/services?tab=hm',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'hm'
                        ]
                    },
                    {
                        'title': 'Техническая охрана',
                        'url': '/services?tab=th',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'th'
                        ]
                    },
                    {
                        'title': 'Изготовление спецодежды',
                        'url': '/services?tab=ds',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'ds'
                        ]
                    },
                    {
                        'title': 'Консультационные и юридические услуги',
                        'url': '/services?tab=cs',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'cs'
                        ]
                    }
                ]
            },
            { 'title': 'Наши цены', 'url': '/prices' },
            {
                'title': 'Статьи',
                'url': '/articles',
                'tabs': [
                    {
                        'title': article.title_ru,
                        'url': f'/articles/{article.id}'
                    } for article in articles
                ]
            },
            { 'title': 'Контакты', 'url': '/contacts' },
            { 'title': 'Документы', 'url': '/documents' },
        ]
    },
    'EN': {
        **global_data['EN'],
        'title': 'Карта сайта',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Карты сайта', 'url': '#'}
        ],

        'linksList': [
            { 'title': 'Главная', 'url': '/' },
            {
                'title': 'О нас',
                'url': '/about',
                'tabs': [
                    {'title': 'История', 'url': '/about?tab=history'},
                    {'title': 'Наш арсенал', 'url': '/about?tab=arsenal'},
                    {'title': 'Наши клиенты', 'url': '/about?tab=clients'},
                    {'title': 'Отзывы', 'url': '/about?tab=feedbacks'},
                    {'title': 'Вакансии', 'url': '/about?tab=vacancies'},
                    {'title': 'Галерея', 'url': '/about?tab=galery'},
                ]
            },
            { 'title': 'Новости', 'url': '/news' },
            {
                'title': 'Услуги',
                'url': '/services',
                'tabs': [
                    {
                        'title': 'Oхранные услуги',
                        'url': '/services?tab=hm',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'hm'
                        ]
                    },
                    {
                        'title': 'Техническая охрана',
                        'url': '/services?tab=th',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'th'
                        ]
                    },
                    {
                        'title': 'Изготовление спецодежды',
                        'url': '/services?tab=ds',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'ds'
                        ]
                    },
                    {
                        'title': 'Консультационные и юридические услуги',
                        'url': '/services?tab=cs',
                        'big_tab': True,
                        'services': [
                            {
                                'title': service.title_ru,
                                'url': f'/services/{service.id}'
                            } for service in services if service.type == 'cs'
                        ]
                    }
                ]
            },
            { 'title': 'Наши цены', 'url': '/prices' },
            {
                'title': 'Статьи',
                'url': '/articles',
                'tabs': [
                    {
                        'title': article.title_ru,
                        'url': f'/articles/{article.id}'
                    } for article in articles
                ]
            },
            { 'title': 'Контакты', 'url': '/contacts' },
            { 'title': 'Документы', 'url': '/documents' },
        ]
    }
}
