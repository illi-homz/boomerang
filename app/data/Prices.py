from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'title': 'Наши цены',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Наши цены', 'url': '#'}
        ],
    },
    'EN': {
        **global_data['EN'],
        'title': 'Our prices',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Our prices', 'url': '#'}
        ],
    }
}
