from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],

        'title': 'Полезные ссылки',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Полезные ссылки', 'url': '#'}
        ],

        'links': [
            {
                'title': 'Интернет-магазин Магнитола52.RU',
                'url': {'title': 'magnitola52.ru', 'url': 'http://www.magnitola52.ru'},
                'descs': [
                    'Автосигнализация Starline, Tomahawk, Pandora, Jaguar, Cenmax, Sheriff',
                    'Сигнализация с обратной связью Старлайн, Пандора, Ягуар, Томагавк, Ценмакс, Шериф',
                    'Брелок с автозапуском'
                ]
            },
            {
                'title': 'J-CLUB',
                'url': {'title': 'jayclub.ru', 'url': 'http://www.jayclub.ru'},
            },
            {
                'title': 'Нижегородская Академия Муай Тай',
                'url': {'title': 'namt-boxing.ru', 'url': 'http://www.namt-boxing.ru'},
            },
            {
                'title': 'СДЮШОР ХК «Торпедо»',
                'url': {'title': 'hctorpedo2004.ru', 'url': 'http://www.hctorpedo2004.ru'},
            },
            {
                'title': 'Общественно-политическая газета «Богородская газета»',
                'url': {'title': 'bg52.ru', 'url': 'http://www.bg52.ru'},
            },
            {
                'title': 'Компания ООО "BuildingAuto"',
                'url': {'title': 'buildingauto.ru', 'url': 'http://www.buildingauto.ru'},
            },
            {
                'title': 'Туристическая фирма “Пилигрим - НН”',
                'url': {'title': 'piligrim.nnov.ru', 'url': 'http://www.piligrim.nnov.ru'},
            },
            {
                'title': 'Компания ООО “Лига Плюс”',
                'url': {'title': 'liga-plus.ru', 'url': 'http://www.liga-plus.ru'},
            },
            {
                'title': 'Кондитерская “Медовик”',
                'url': {'title': 'medovik52.ru', 'url': 'http://www.medovik52.ru'},
            },
            {
                'title': 'Эволюция сознания',
                'url': {'title': 'soznanie.nnov.ru', 'url': 'http://www.soznanie.nnov.ru'},
            },
            {
                'title': 'iMafia2 - Бесплатная онлайн-игра "Мафия" для iOS',
                'url': {'title': 'imafia2.ru', 'url': 'http://www.www.imafia2.ru'},
                'description': 'Пошаговая ролевая игра Мафия для мобильных телефонов Apple iPhone и планшетов Apple iPad. Выступи на стороне мафии или мирных жителей - покажи всем, кто на самом деле правит этим городом!'
            }
        ]
    },
    'EN': {
        **global_data['EN'],

        'title': 'Useful links',

        'breadCrumbs': [
            {'title': 'The main', 'url': '/'},
            {'title': 'Useful links', 'url': '#'}
        ],

        'links': [
            {
                'title': 'Online store Magnitola52.RU',
                'url': {'title': 'magnitola52.ru', 'url': 'http://www.magnitola52.ru'},
                'descs': [
                  'Car alarm Starline, Tomahawk, Pandora, Jaguar, Cenmax, Sheriff',
                     'Alarm with feedback Starline, Pandora, Jaguar, Tomahawk, Zenmax, Sheriff',
                     'Keychain with auto start'
                ]
            },
            {
                'title': 'J-CLUB',
                'url': {'title': 'jayclub.ru', 'url': 'http://www.jayclub.ru'},
            },
            {
                'title': 'Nizhny Novgorod Academy of Muay Thai',
                'url': {'title': 'namt-boxing.ru', 'url': 'http://www.namt-boxing.ru'},
            },
            {
                'title': 'Olympic Hockey Training School for Children and Adolescent "Torpedo"',
                'url': {'title': 'hctorpedo2004.ru', 'url': 'http://www.hctorpedo2004.ru'},
            },
            {
                'title': 'Social and political newspaper "Bogorodskaya Gazeta"',
                'url': {'title': 'bg52.ru', 'url': 'http://www.bg52.ru'},
            },
            {
                'title': ''' BuildingAuto Ltd ''',
                'url': {'title': 'buildingauto.ru', 'url': 'http://www.buildingauto.ru'},
            },
            {
                'title': 'Travel company "Pilgrim - NN"',
                'url': {'title': 'piligrim.nnov.ru', 'url': 'http://www.piligrim.nnov.ru'},
            },
            {
                'title': '“Liga Plus” Ltd',
                'url': {'title': 'liga-plus.ru', 'url': 'http://www.liga-plus.ru'},
            },
            {
                'title': 'Confectionery "Medovik"',
                'url': {'title': 'medovik52.ru', 'url': 'http://www.medovik52.ru'},
            },
            {
                'title': 'Evolution of Consciousness',
                'url': {'title': 'soznanie.nnov.ru', 'url': 'http://www.soznanie.nnov.ru'},
            },
            {
                'title': 'iMafia2 - Free Online Mafia Game for iOS',
                'url': {'title': 'imafia2.ru', 'url': 'http://www.www.imafia2.ru'},
                'description': 'Mafia turn-based RPG game for Apple iPhone mobile phones and Apple iPad tablets. Take the side of the mafia or civilians - show everyone who really rules this city! '
            }
        ]
    }
}