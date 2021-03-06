from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=50, default='')
    img = models.ImageField(upload_to='galery', verbose_name='Фото')

    def __str__(self):
        return self.title