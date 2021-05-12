from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],
        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Статьи', 'url': '/articles'},
            {'title': '', 'url': '#'}
        ],
        'toUp': 'Наверх',
        'readStyle': 'Страница переведена в режим для чтения'
    },
    'EN': {
        **global_data['EN'],
        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Articles', 'url': '/articles'},
            {'title': '', 'url': '#'}
        ],
        'toUp': 'Up',
        'readStyle': 'The page is switched to read mode'
    }
}
