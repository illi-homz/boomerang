from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],

        'title': 'Полезные ссылки',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Полезные ссылки', 'url': '#'}
        ],
    },
    'EN': {
        **global_data['EN'],

        'title': 'Useful links',

        'breadCrumbs': [
            {'title': 'The main', 'url': '/'},
            {'title': 'Useful links', 'url': '#'}
        ],
    }
}