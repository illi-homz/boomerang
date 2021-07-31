from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'title': 'Новости',
        'more': 'Подробнее',
        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Новости', 'url': '#'}
        ],
    },
    'EN': {
        **global_data['EN'],
        'title': 'News',
        'more': 'More',
        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'News', 'url': '#'}
        ],
    }
}
