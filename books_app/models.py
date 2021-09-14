from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=124, verbose_name='Tytuł')
    author = models.CharField(max_length=124, verbose_name='autor', null=True)
    publshed_date = models.DateField(verbose_name='Data publikacji', null=True)
    isbn = models.CharField(max_length=124, verbose_name='Numer ISBN', null=True)
    page_count = models.IntegerField(verbose_name='Liczba stron', null=True)
    thumbnail = models.URLField(verbose_name='Link do okładki', null=True)
    publication_language = models.CharField(max_length=124, verbose_name='Język publikacji', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-list')
