from django.db import models


class Client(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    img = models.ImageField(upload_to='galery/', verbose_name='Фото')

    def __str__(self):
        return self.title_ru

    def title(self):
        return {
            'RU': self.title_ru,
            'EN': self.title_en,
        }
