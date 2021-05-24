from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],
        'title': 'Страница не найдена',
        'text': 'Упс, похоже данной страницы не существует',
        'btn': 'вернуться На главную'
    },
    'EN': {
        **global_data['EN'],
        'title': 'Page not found',
        'text': 'Oops, this page doesn\'t seem to exist',
        'btn': 'Go back to the main page'
    }
}