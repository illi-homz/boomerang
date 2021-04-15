from django.db import models

class New(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    desc = models.CharField(max_length=300, verbose_name='Описание', default='')
    text = models.TextField(default='', verbose_name='Формотированный текст')
    date = models.DateTimeField(auto_now=True, blank=True)
    img = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='Картинка')

    def __str__(self):
        return f'{self.date.strftime("%d.%m.%Y %H:%M")} - {self.desc}'
