import datetime
# from django.conf import settings

def set_cookie(response, key, value, days_expire=100):
    max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        # domain=settings.SESSION_COOKIE_DOMAIN,
        # secure=settings.SESSION_COOKIE_SECURE or None,
    )
    return response
