import pytest

from main import BooksCollector


@pytest.fixture
def books_collector():
    collector = BooksCollector()
    books_with_genre = [
        ['Смерть на ЗиЛе', 'Фантастика'],
        ['Как править миром незаметно от санитаров', 'Детективы'],
    ]
    for name, genre in books_with_genre:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
