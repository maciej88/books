from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = (
            "title", "author", "publshed_date", "isbn", "page_count", "thumbnail", "publication_language"
        )

