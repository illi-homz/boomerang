def get_locale(request):
    if ('locale' in request.COOKIES):
        locale = request.COOKIES['locale']
    else:
        locale = 'RU'
    return locale
