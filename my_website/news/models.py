from django.db import models

# Create your models here.


class Artiles(models.Model):
    title = models.CharField('Topic name', max_length=40)
    anons = models.CharField('Announcement', max_length=300)
    title_text = models.TextField('Article')
    date = models.DateTimeField('Publication time')

    def __str__(self):
        return f'News: {self.title}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
