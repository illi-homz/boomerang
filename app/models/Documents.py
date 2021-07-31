from django.db import models

REGULAR = 'reg'
TECHNICAL = 'tech'

TYPES = [
    (REGULAR, 'Общая'),
    (TECHNICAL, 'Техническая'),
]

class Document(models.Model):
    title = models.CharField(
        max_length=200 ,
        verbose_name='Название лиценции, рус',
        default='Лицензия'
    )
    type = models.CharField(max_length=4, choices=TYPES, default=REGULAR)
    date = models.DateField(verbose_name='Дата получения')
    img = models.ImageField(upload_to='documents', verbose_name='Картинка')

    def __str__(self):
        return f'{self.date.strftime("%d.%m.%Y")} - {self.title}'
