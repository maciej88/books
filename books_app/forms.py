from django import forms
from .models import Book


class BookAddForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'publication_date': forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'type': 'date'}, format='%d/%m%Y')
        }


class BookApiForm(forms.Form):
    key_words = forms.CharField(
        max_length=124, label='Szukaj'
    )
