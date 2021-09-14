import pytest

from django.test import Client

from books_app.models import Book


@pytest.fixture
def client():
    client = Client()
    return client

