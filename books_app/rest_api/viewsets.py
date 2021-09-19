from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from books_app.rest_api.serializers import BookSerializer
from books_app.models import Book
from books_app.filters import BookFilter

# Create your views here.
class BookView(generics.ListAPIView):
    """
    Rest-framework list of books view + filtering system
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = BookFilter
    ordering_fields = ['publication_date']