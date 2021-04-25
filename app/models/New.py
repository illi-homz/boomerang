from django.db import models

class New(models.Model):
    title_ru = models.CharField(
        max_length=200,
        verbose_name='Заголовок, ру',
        blank=True,
        null=True
    )
    title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок, англ',
        blank=True,
        null=True
    )
    desc_ru = models.CharField(
        max_length=300,
        verbose_name='Описание, ру',
        blank=True,
        null=True
    )
    desc_en = models.CharField(
        max_length=300,
        verbose_name='Описание, англ',
        blank=True,
        null=True
    )
    text_ru = models.TextField(
        default='',
        verbose_name='Формотированный текст, ру',
        blank=True,
        null=True
    )
    text_en = models.TextField(
        default='',
        verbose_name='Формотированный текст, англ',
        blank=True,
        null=True
    )
    date = models.DateTimeField(auto_now=True, blank=True)
    img = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='Картинка')

    def __str__(self):
        return f'{self.date.strftime("%d.%m.%Y %H:%M")} - {self.title_ru}'

    def title(self):
        return {
            'RU': self.title_ru,
            'EN': self.title_en
        }

    def desc(self):
        return {
            'RU': self.desc_ru,
            'EN': self.desc_en
        }

    def text(self):
        return {
            'RU': self.text_ru,
            'EN': self.text_en
        }
