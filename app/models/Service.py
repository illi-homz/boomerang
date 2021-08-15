from django.db import models

class Service(models.Model):
    HUMAN = 'hm'
    TECHNICAL = 'th'
    # DRESS = 'ds'
    CONSULTATION = 'cs'

    TYPES = [
        (HUMAN, 'Oхранные услуги'),
        (TECHNICAL, 'Техническая охрана'),
        # (DRESS, 'Изготовление спецодежды'),
        (CONSULTATION, 'Консультационные и юридические услуги'),
    ]

    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    desc_ru = models.CharField(max_length=300, blank=True, default='')
    desc_en = models.CharField(max_length=300, blank=True, default='')
    text_ru = models.TextField(blank=True, null=True)
    text_en = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=2, choices=TYPES, default=HUMAN)
    price = models.SmallIntegerField(default=0, blank=True, null=True)
    img = models.ImageField(upload_to='services', verbose_name='Картинка')

    def __str__(self):
        return self.title_ru

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
