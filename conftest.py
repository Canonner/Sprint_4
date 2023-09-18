import pytest

from main import BooksCollector


@pytest.fixture
def books_collector():
    collector = BooksCollector()
    books_with_genre = [
        ['Смерть на ЗиЛе', 'Фантастика'],
        ['Как победить при Бородино в 6 палате', ''],
        ['Операция ЪУЪ', 'Комедии'],
        ['Задачник по албанскому мату с решениями', 'Мультфильмы'],
        ['Как править миром незаметно от санитаров', 'Детективы'],
        ['101 рецепт жарки мяса в ядерном реакторе', 'Ужасы']
    ]
    for name, genre in books_with_genre:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
