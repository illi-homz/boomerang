from django.db import models

class Price(models.Model):
    title_ru = models.CharField(
        max_length=200 ,
        verbose_name='Название услуги, рус',
        blank=True,
        null=True
    )
    title_en = models.CharField(
        max_length=200 ,
        verbose_name='Название услуги, англ',
        blank=True,
        null=True
    )
    price_ru = models.CharField(
        max_length=50,
        verbose_name='цена, рус',
        blank=True,
        null=True
    )
    price_en = models.CharField(
        max_length=50,
        verbose_name='цена, англ',
        blank=True,
        null=True
    )
    img = models.ImageField(upload_to='prices', verbose_name='Картинка')

    def __str__(self):
        return self.title_ru

    def title(self):
        return {
            'RU': self.title_ru,
            'EN': self.title_en
        }

    def price(self):
        return {
            'RU': self.price_ru,
            'EN': self.price_en
        }
