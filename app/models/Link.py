from django.db import models


class Link(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    url = models.TextField()
    description_ru = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_ru

    def title(self):
        return {
            'RU': self.title_ru,
            'EN': self.title_en,
        }
    
    def description(self):
        return {
            'RU': self.description_ru,
            'EN': self.description_en,
        }