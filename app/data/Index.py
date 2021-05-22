from django.conf import settings
static = settings.STATIC_URL
from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],
        'title': 'Главная',
        'banner': {
            'title': 'Пультовая охрана <br>в Нижнем Новгороде',
            'data': [
                {'count': 27, 'text': 'лет на рынке <br>охранных предприятий'},
                {'count': 3000, 'text': 'охраняемых объектов'},
                {'count': 52, 'text': 'единицы <br>огнестрельного оружия'},
                {'count': 750, 'text': 'наш штат работников в настоящее время'},
            ],
            'bg': static + 'img/main-banner'
        },
        'services': {
            'title': 'услуги',
            'all_services': 'ВСЕ УСЛУГИ',
            'desc': 'Группа охранных предприятий "Бумеранг" прочно обосновалось на рынке предоставления охранных услуг, более чем двадцатилетнюю работу создало себе имидж надежного, высокоинтеллектуального охранного предприятия.',
            'read_more': 'Читать подробнее',
            'slides': []
        },
        'about': {
            'title': 'о нас',
            'text_list': [
                'Руководящий состав группы охранных предприятий «Бумеранг» имеет большой опыт организации эффективной охраны предприятий различного профиля. На предприятии имеется резерв для оперативной замены и усиления постов охраны. Работа охранников на объектах контролируется круглосуточно. С 17-00 до 9-00 работает оперативный дежурный, которому каждый час докладывается оперативная обстановка на всех объектах. Также, в ночное время осуществляются проверки несения службы сотрудниками отдела внутреннего контроля.',
                'Соучредителями ЧОО «МОП Центр» выступают охранные организации, расположенные в каждом субъекте Российской Федерации в Центральном, Приволжском, Северо-Западном, Южном и Северо-Кавказском федеральных округах, а также ряд охранных организаций в Дальне-Восточном и Сибирском федеральных округах; Объединение охранных организаций в рамках проекта «МОП Центр» направлено на координацию защиты интересов клиентов, работающих в нескольких субъектах Российской Федерации.'
            ],
            'img': static + 'img/index/about/office',
            'link': {
                'text': 'читать подробнее',
                'url': '/about?tab=history'
            }
        },
        'promo': {
            'title': 'Акции',
            'promos': [
                {
                    'title': 'Скидка 30% на охрану первым клиентам',
                    'text': 'Надежность здесь и сейчас с первого звонка!',
                    'img': static + 'img/index/promo/promo'
                },
                {
                    'title': 'Скидка 30% на установку видео-камер',
                    'text': 'Камеры видео-наблюдения высокого разрешения!',
                    'img': static + 'img/index/promo/camera'
                },
                {
                    'title': 'Скидка 20% на любую услугу',
                    'text': 'Ваша безопасность за доступную цену!',
                    'img': static + 'img/index/promo/promo'
                },
            ],
        },
        'news': {
            'title': 'Новости',
            'more_details': 'Подробнее'
        }
    },
    'EN': {
        **global_data['EN'],
        'title': 'Main',
        'banner': {
            'title': 'Console security <br>in Nizhny Novgorod',
            'data': [
                {'count': 27, 'text': 'years on the market <br>of security companies'},
                {'count': 3000, 'text': 'protected objects'},
                {'count': 52, 'text': 'units firearms'},
                {'count': 750, 'text': 'our workforce is currently'},
            ],
            'bg': static + 'img/main-banner'
        },
        'services': {
            'title': 'services',
            'all_services': 'ALL SERVICES',
            'desc': 'The group of security companies "Boomerang" for more than twenty years of existence has created an image of a reliable, highly intelligent security company.',
            'read_more': 'Read more',
            'slides': []
        },
        'about': {
            'title': 'about us',
            'text_list': [
                'The management of the group of security companies "Boomerang" has extensive experience in organizing effective security for facilities of various profiles. The enterprise has a reserve for prompt replacement and strengthening of security posts. The work of security guards at the facilities is monitored around the clock. From 17-00 to 9-00 an operational duty officer works, to whom the operational situation at all objects is reported every hour. Also, at night, inspections of service by employees of the internal control department are carried out.',
                'The co-founders of the MOP Center private limited liability company are security organizations located in each constituent entity of the Russian Federation in the Central, Volga, North-West, South and North-Caucasian Federal Districts, as well as a number of security organizations in the Far-Eastern and Siberian Federal Districts; The association of security organizations within the framework of the MOP Center project is aimed at coordinating the protection of the interests of clients working in several constituent entities of the Russian Federation.'
            ],
            'img': static + 'img/index/about/office',
            'link': {
                'text': 'read more',
                'url': '/about?tab=history'
            }
        },
        'promo': {
            'title': 'Promos',
            'promos': [
                {
                    'title': '30\% discount on security for first customers',
                    'text': 'Reliability here and now from the first call!',
                    'img': static + 'img/index/promo/promo'
                },
                {
                    'title': '30\% discount on video cameras installation',
                    'text': 'High Definition Video Surveillance Cameras!',
                    'img': static + 'img/index/promo/camera'
                },
                {
                    'title': '20\% discount on any service',
                    'text': 'Your safety at an affordable price!',
                    'img': static + 'img/index/promo/promo'
                },
            ],
        },
        'news': {
            'title': 'News',
            'more_details': 'More details'
        }
    },
}
