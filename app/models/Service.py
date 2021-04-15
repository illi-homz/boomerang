from django.db import models

TYPES = [
    ('human', 'Oхранные услуги'),
    ('TECHNICAL', 'Техническая охрана'),
    ('dress', 'Изготовление спецодежды'),
    ('consultation', 'Консультационные и юридические услуги'),
]

class Service(models.Model):
    HUMAN = 'hm'
    TECHNICAL = 'th'
    DRESS = 'ds'
    CONSULTATION = 'cs'

    TYPES = [
        (HUMAN, 'Oхранные услуги'),
        (TECHNICAL, 'Техническая охрана'),
        (DRESS, 'Изготовление спецодежды'),
        (CONSULTATION, 'Консультационные и юридические услуги'),
    ]

    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=300, default='', blank=True)
    text = models.TextField(default='')
    type = models.CharField(max_length=2, choices=TYPES, default=HUMAN)
    price = models.SmallIntegerField(default=0)
    img = models.ImageField(upload_to='services', verbose_name='Картинка')

    def __str__(self):
        return self.title
