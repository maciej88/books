from django import forms


class BookAddForm(forms.Form):
    title = forms.CharField(max_length=124, label='Tytuł')
    author = forms.CharField(max_length=124, label='Autor/Autorzy')
    publshed_date = forms.DateField(label='Data publikacji', widget=forms.DateInput())
    page_count = forms.IntegerField(label='Liczba stron')
    thumbnail = forms.URLField(label='Link do okładki')
    publication_language = forms.CharField(max_length=124, label='Język publikacji')
    isbn_13 = forms.CharField(max_length=124, label='ISBN 13', required=False)
    isbn_10 = forms.CharField(max_length=124, label='ISBN 10', required=False)
    other = forms.CharField(max_length=124, label='Inny numer identyfikacji', required=False)