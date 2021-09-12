from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import BookAddForm
from .models import Book
from .filters import BookFilter

from django.views.generic import ListView, CreateView, UpdateView


# Create your views here.
# class BooksListView(View):
#     def get(self, request):
#         books = Book.objects.get.all()
#         myFilter = BookFilter()
#         context = {"books": books, "myFilter": myFilter}
#         return render(request, 'book_list.html', context)


class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = "book_list.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filter']= BookFilter(self.request.GET, queryset=self.get_queryset())
        return context




class BookAddView(CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'book_add.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_update.html'

