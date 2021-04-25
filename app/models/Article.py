from django.db import models


PERSONAL_SAFETY = 'PSS'
FOR_DRIVERS = 'DRV'
PROTECTION_OF_OBJECTS = 'OBJ'
PRIVATE_SECURITY = 'PVS'
CARGO_SECURITY_AND_ESCORT = 'CSE'
FIRE_SAFETY = 'FRS'
SECURITY_SYSTEMS = 'SSY'
PSYCHOLOGY = 'PSY'

CATEGORYES = {
    'RU': [
        (PERSONAL_SAFETY, 'Личная безопасность'),
        (FOR_DRIVERS, 'Водителям'),
        (PROTECTION_OF_OBJECTS, 'Охрана объектов'),
        (PRIVATE_SECURITY, 'Личная охрана'),
        (CARGO_SECURITY_AND_ESCORT, 'Охрана и сопровождение грузов'),
        (FIRE_SAFETY, 'Пожарная безопасность'),
        (SECURITY_SYSTEMS, 'Охранные системы'),
        (PSYCHOLOGY, 'Психология'),
    ],
    'EN': [
        (PERSONAL_SAFETY, 'Personal safety'),
        (FOR_DRIVERS, 'For drivers'),
        (PROTECTION_OF_OBJECTS, 'Protection of objects'),
        (PRIVATE_SECURITY, 'Private security'),
        (CARGO_SECURITY_AND_ESCORT, 'Cargo security and escort'),
        (FIRE_SAFETY, 'Fire safety'),
        (SECURITY_SYSTEMS, 'Security systems'),
        (PSYCHOLOGY, 'Psychology'),
    ],
}

class Article(models.Model):
    title_ru = models.CharField(max_length=200, null=True, blank=True)
    title_en = models.CharField(max_length=200, null=True, blank=True)
    text_ru = models.TextField(default='', null=True, blank=True)
    text_en = models.TextField(default='', null=True, blank=True)
    category = models.CharField(max_length=3, choices=CATEGORYES['RU'], default=PERSONAL_SAFETY)

    def __str__(self):
        return self.title_ru

    def title(self):
        return {
            'RU': self.title_ru,
            'EN': self.title_en
        }

    def text(self):
        return {
            'RU': self.text_ru,
            'EN': self.text_en
        }
