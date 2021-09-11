from django import forms
from .models import Book


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'publshed_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})
        }
