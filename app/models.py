from django.db import models

class New(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=300, default='')
    text = models.TextField(default='')
    date = models.DateTimeField(auto_now=True, blank=True)
    img = models.ImageField(upload_to='news/%Y/%m/%d/')

    def __str__(self):
        return f'{self.date.strftime("%d.%m.%Y %H:%M")} - {self.desc}'
