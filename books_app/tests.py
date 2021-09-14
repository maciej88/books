import pytest
import datetime

from .models import Book

# Create your tests here.
REQUEST_DATA_SET = (
    {'title': 'Hobbit',
     'author': 'Tolkien',
     'publication_date': datetime.date(2021, 1, 2),
     'isbn': '123456789',
     'page_count': int(555),
     'thumbnail': 'http://books.google.pl/books?id=DqLPAAAAMAAJ&dq=Hobbit&hl=&source=gbs_api',
     'publication_language': 'Polski'}
)


@pytest.mark.django_db
def test_book_create(client):
    """
    This test should pass
    """
    request_url = '/create/'
    response = client.post(request_url, REQUEST_DATA_SET)
    assert response.status_code == 302, 'Check isn request contains 302 http status'
    book = Book.objects.get(**REQUEST_DATA_SET)
    assert book.title == REQUEST_DATA_SET['title']
    assert book.author == REQUEST_DATA_SET['author']
    assert book.publication_date == REQUEST_DATA_SET['publication_date']
    assert book.isbn == REQUEST_DATA_SET['isbn']
    assert book.page_count == REQUEST_DATA_SET['page_count']
    assert book.thumbnail == REQUEST_DATA_SET['thumbnail']
    assert book.publication_language == REQUEST_DATA_SET['publication_language']


@pytest.mark.django_db
def test_book_create_half(client):
    """
    This test should failed!!!
    """
    request_url = '/create/'
    book_data = {'title': 'Hobbit', 'author': 'Tolkien'}
    response = client.post(request_url, book_data)
    assert response.status_code == 302, 'Check isn request contains 302 http status'
    book = Book.objects.get(**book_data)
    assert book.title == REQUEST_DATA_SET['title']
    assert book.author == book_data['author']
