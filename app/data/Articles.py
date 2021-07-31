from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],
        'title': 'Статьи',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Статьи', 'url': '#'}
        ],

        'category': 'Категория',
        'theme': 'Тема',
        'read': 'Читать',
        'load_more': 'Загрузить еще',
        'all': 'Все',
        'any': 'Любая'
    },
    'EN': {
        **global_data['EN'],
        'title': 'Articles',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Articles', 'url': '#'}
        ],

        'category': 'Category',
        'theme': 'Theme',
        'read': 'Read',
        'load_more': 'Load more',
        'all': 'All',
        'any': 'Any'
    }
}
