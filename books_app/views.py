from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import BookAddForm
from .models import Book, Identifiers

from django.views.generic import ListView


# Create your views here.
class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = "book_list.html"

class BookAddView(View):
    def get(self, request):
        form = BookAddForm()
        return render(request, 'book_add.html', {'form':form})

    def post(self, request):
        form = BookAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author =  form.cleaned_data['author']
            publshed_date =  form.cleaned_data['published_date']
            page_count =  form.cleaned_data['page_count']
            thumbnail =  form.cleaned_data['thumbnail']
            publication_language =  form.cleaned_data['publication_language']
            isbn_13 =  form.cleaned_data['isbn_13']
            isbn_10 =  form.cleaned_data['isbn_10']
            other =  form.cleaned_data['other']
            identifiers = Identifiers.objects.create(isbn_13=isbn_13, isbn_10=isbn_10, other=other)
            Book.objects.create(
                title=title, author=author, publshed_date=publshed_date, isbn=identifiers,
                page_count=page_count, thumbnail=thumbnail, publication_language=publication_language)
            return redirect('')
        return HttpResponse(str(form.cleaned_data))
