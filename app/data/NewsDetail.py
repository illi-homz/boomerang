from .Global import data as global_data


data = {
    'RU': {
        **global_data['RU'],
        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Новости', 'url': '/news'},
            {'title': '', 'url': '#'}
        ],
        'readSame': 'Читайте так же'
    },
    'EN': {
        **global_data['EN'],
        'breadCrumbs': [
            {'title': 'Main page', 'url': '/'},
            {'title': 'News', 'url': '/news'},
            {'title': '', 'url': '#'}
        ],
        'readSame': 'Read the same'
    }
}
