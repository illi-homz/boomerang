from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'title': 'Наши акции',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Наши акции', 'url': '#'}
        ],
    },
    'EN': {
        **global_data['EN'],
        'title': 'Our stocks',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Our stocks', 'url': '#'}
        ],
    }
}
