from django.db import models


# Create your models here.
class Identifiers(models.Model):
    isbn_13 = models.CharField(max_length=124, blank=True, unique=True)
    isbn_10 = models.CharField(max_length=124, blank=True, unique=True)
    other = models.CharField(max_length=124, blank=True, unique=True)


class Book(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=124, blank=True)
    publshed_date = models.CharField(max_length=20, blank=True)
    isbn_number = models.OneToOneField(Identifiers, on_delete=models.CASCADE, unique=True)
    page_count = models.IntegerField(blank=True)
    thumbnail = models.URLField(blank=True)
    publication_language = models.CharField(max_length=124, blank=True)

    def __str__(self):
        return self.title