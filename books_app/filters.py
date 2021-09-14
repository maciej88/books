import django_filters
from django import forms
from django_filters import DateFilter, CharFilter

from .models import Book


class BookFilter(django_filters.FilterSet):
    fromdate = DateFilter(field_name="publication_date", lookup_expr='gte', label='Od daty',
                          widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    todate = DateFilter(field_name="publication_date", lookup_expr='lte', label='Do daty',
                        widget=forms.DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}))
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Tytuł')
    author = CharFilter(field_name='author', lookup_expr='icontains', label='Autor')
    publication_language = CharFilter(field_name='title', lookup_expr='icontains', label='Język publikacji')

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['isbn', 'publication_date', 'page_count', 'thumbnail']
