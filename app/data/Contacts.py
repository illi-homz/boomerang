from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'title': 'Контакты',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Статьи', 'url': '#'}
        ],

        'postAdressTitle': 'Почтовый адрес',
        'postAdress': '603093, г. Н.Новгород, ул. Яблоневая, д. 18',

        'email': 'bumerang52@list.ru',

        'officeTitle': 'Офис',
        'office': '603093, г. Нижний Новгород, ул. Яблоневая, д. 18',

        'phonesTitle': 'Телефоны',
        'phones': ['+7 (831) 28-28-911,', '28-26-112,', '28-26-110'],

        'cooperationTitle': 'По вопросам сотрудничества',
        'cooperation': '+7 (831) 424-08-18 (круглосуточно)',
        'cooperationTel': '+7 (831) 424-08-18',

        'vkTitle': 'Мы Вконтакте',
        'vk': 'vk.com/52bumerang52'
    },
    'EN': {
        **global_data['EN'],
        'title': 'Contacts',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Articles', 'url': '#'}
        ],

        'postAdressTitle': 'Post adress',
        'postAdress': '603093, N. Novgorod, st. Yablonevaya, 18',

        'email': 'bumerang52@list.ru',

        'officeTitle': 'Office',
        'office': '603093, N. Novgorod, st. Yablonevaya, 18',

        'phonesTitle': 'Phones',
        'phones': ['+7 (831) 28-28-911,', ' 28-26-112,', ' 28-26-110'],

        'cooperationTitle': 'Cooperation',
        'cooperation': '+7 (831) 424-08-18 (around the clock)',
        'cooperationTel': '+7 (831) 424-08-18',

        'vkTitle': 'We are on Vkontakte',
        'vk': 'vk.com/52bumerang52'
    }
}
