from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django.views.generic import CreateView, ListView


# Create your views here.
class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = "book_list.html"

class BookAddView(CreateView):
    model = Book



