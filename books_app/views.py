from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import BookAddForm
from .models import Book

from django.views.generic import ListView, CreateView


# Create your views here.
class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = "book_list.html"


class BookAddView(CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'book_add.html'


