from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import BookAddForm, BookApiForm
from .models import Book
from .filters import BookFilter
from .google_api import books_to_database


class BooksListView(ListView):
    model = Book
    paginate_by = 10
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


class GoogleApiView(FormView):
    template_name = "book_api.html"
    form_class = BookApiForm
    success_url = reverse_lazy("book-list")

    def form_valid(self, form):
        key_words = form.cleaned_data["key_words"]
        if not key_words:
            redirect("google-api")
        books_to_database(key_words)
        return redirect("book-list")
