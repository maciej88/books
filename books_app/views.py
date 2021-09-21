from django.views.generic import ListView, CreateView, UpdateView

from .forms import BookAddForm
from .models import Book
from .filters import BookFilter


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
