from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=124, verbose_name='Tytuł')
    author = models.CharField(max_length=124, verbose_name='autor')
    publshed_date = models.DateField(verbose_name='Data publikacji')
    isbn = models.CharField(max_length=124, verbose_name='Numer ISBN')
    page_count = models.IntegerField(verbose_name='Liczba stron')
    thumbnail = models.URLField(null=True, blank=True, verbose_name='Link do okładki')
    publication_language = models.CharField(max_length=124, verbose_name='Język publikacji')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-list')
