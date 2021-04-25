from django.db import models


class Photo(models.Model):
    img = models.ImageField(upload_to='galery/', verbose_name='Фото')
