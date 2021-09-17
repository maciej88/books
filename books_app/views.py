from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django.contrib import messages


from .forms import BookAddForm, BookApiForm
from .models import Book
from .filters import BookFilter
from .serializers import BookSerializer


class BooksListView(ListView):
    model = Book
    template_name = "book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BookAddView(CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'book_add.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_update.html'


class GoogleApiView(View):
    """
    Google api View for collect data
    """
    template_name = "book_api.html"

    def get(self, request):
        form = BookApiForm()
        return render(request, "book_api.html", {'form': form})

    def post(self, request):
        form = BookApiForm(request.POST)
        if form.is_valid():
            key_words = request.POST['key_words']
            key_words = key_words.replace(' ', '+')
            google_url = HttpResponseRedirect(f'https://www.googleapis.com/books/v1/volumes?q={key_words}')
            if google_url.status_code == 200:
                resoult = google_url.json()

                for item in resoult['items']: #check space in db
                    if Book.objects.filter(
                            title=item['volumeInfo']['title']):
                        messages.warning(
                            request, f"Książka '{key_words}' znajduje się już w bazie danych")
                        return render('book_api.html', {'form': form})
                    else:
                        if 'authors' in item['volumeInfo']:
                            book = Book()
                            book.title = item['volumeInfo']['title']
                            if 'publishedDate'in item['volumeInfo']:
                                book.publication_date = item['volumeInfo']['publishedDate']
                            for author in item['volumeInfo']['authors']:
                                author_create = Book.objects.get_or_create(
                                    name=author)[0]
                                book.objects.create(author_create=author_create)
                            for item['type'] in item['volumeInfo']['industryIdentifiers']:
                                if item['type'] == 'ISBN_13':
                                    isbn = item['industryIdentifiers']['identifier']
                                else:
                                    isbn = None
                                book.objects.create(isbn=isbn)
                            if 'pageCount' in item['volumeInfo']:
                                page_count=item['volumeInfo']['pageCount']
                                book.objects.create(page_count=page_count)
                            if 'thumbnail' in item['volumeInfo']['imageLinks']:
                                thumbnail = item['volumeInfo']['thumbnail']
                                book.objects.create(thumbnail=thumbnail)
                            if 'language' in item['volumeInfo']['language']:
                                publication_language = item['volumeInfo']['language']
                                book.objects.create(publication_language=publication_language)
                            book.save()
                messages.success(request, 'Dodano nową pozycję')
                return HttpResponseRedirect(redirect('book-list'))
            errors = ('Coś poszło nie tak')
            return render(request, 'book_api.html', {'form': form, 'messages': errors})


class BookView(generics.ListAPIView):
    """
    Rest-framework list of books view + filtering system
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = BookFilter
    ordering_fields = ['publication_date']
