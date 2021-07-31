from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'title': 'Контакты',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Статьи', 'url': '#'}
        ],

        'emails': [
            {
                'title': 'bumerang52@list.ru,',
                'email': 'bumerang52@list.ru',
            },
            {
                'title': 'ohrana@bumerang52.ru,',
                'email': 'ohrana@bumerang52.ru',
            },
            {
                'title': 'kk.mashin@bumerang52.ru',
                'email': 'kk.mashin@bumerang52.ru',
            }
        ],

        'addressTitle': 'Адрес',
        'address': '603093, г. Нижний Новгород, ул. Яблоневая, д. 18',

        'phonesTitle': 'Телефоны',
        'phones': [
            {
                'title': '+7 (831) 28-28-911,',
                'phone': '+7 (831) 28-28-911'
            },
            {
                'title': '+7 (953) 571-88-77',
                'phone': '+7 (953) 571-88-77'
            }
        ],

        'vkTitle': 'Мы ВКонтакте',
        'vk': 'vk.com/52bumerang52'
    },
    'EN': {
        **global_data['EN'],
        'title': 'Contacts',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Articles', 'url': '#'}
        ],

        'emails': [
            {
                'title': 'bumerang52@list.ru,',
                'email': 'bumerang52@list.ru',
            },
            {
                'title': 'ohrana@bumerang52.ru,',
                'email': 'ohrana@bumerang52.ru',
            },
            {
                'title': 'kk.mashin@bumerang52.ru',
                'email': 'kk.mashin@bumerang52.ru',
            }
        ],

        'addressTitle': 'Address',
        'address': '603093, N. Novgorod, st. Yablonevaya, 18',

        'phonesTitle': 'Phones',

        'phones': [
            {
                'title': '+7 (831) 28-28-911,',
                'phone': '+7 (831) 28-28-911'
            },
            {
                'title': '+7 (953) 571-88-77',
                'phone': '+7 (953) 571-88-77'
            }
        ],

        'vkTitle': 'We are on VKontakte',
        'vk': 'vk.com/52bumerang52'
    }
}
