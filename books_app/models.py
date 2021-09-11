from django.db import models


# Create your models here.
class Identifiers(models.Model):
    isbn_13 = models.CharField(max_length=124, blank=True, unique=True, null=True)
    isbn_10 = models.CharField(max_length=124, blank=True, unique=True, null=True)
    other = models.CharField(max_length=124, blank=True, unique=True, null=True)


class Book(models.Model):
    title = models.CharField(max_length=124)
    author = models.CharField(max_length=124)
    publshed_date = models.DateField()
    isbn = models.OneToOneField(Identifiers, on_delete=models.CASCADE, unique=True, blank=False)
    page_count = models.IntegerField()
    thumbnail = models.URLField(blank=True, null=True)
    publication_language = models.CharField(max_length=124)

    def __str__(self):
        return self.title