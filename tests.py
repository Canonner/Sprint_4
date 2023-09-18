import pytest

from main import BooksCollector


class TestBooksCollector:

    # Cписок для проверки метода add_new_book - новая книга, повтор новой книги
    # и 4 книги для проверки классов "0", "от 1 до 40", "больше 40" символов - 0, 1, 39, 40 и 41 символ
    books_to_add = [
        'Смерть на ЗиЛе',
        'Смерть на ЗиЛе',
        '',
        'Ъ',
        'Задачник по албанскому мату с решениями',
        'Как править миром незаметно от санитаров',
        '99 рецептов жарки мяса в ядерном реакторе'
    ]

    # 1. Тест для метода add_new_book
    @pytest.mark.parametrize('name', books_to_add)
    def test_add_new_book_seven_books_four_added(self, name):
        collector = BooksCollector()
        for i in self.books_to_add:
            collector.add_new_book(i)
        assert collector.get_books_genre() == {
            'Смерть на ЗиЛе': '',
            'Ъ': '',
            'Задачник по албанскому мату с решениями': '',
            'Как править миром незаметно от санитаров': ''
        }

    # 2. Тест для метода set_book_genre - параметризация

    # Cписок для проверки метода - 6 книг с валидными названиями, у одной из которых нет жанра,
    # одна книга с невалидным названем
    # одна книга с валидным названием и невалидным жанром
    eight_books_with_genre = [
        ['Смерть на ЗиЛе', 'Фантастика'],
        ['Как победить при Бородино в 6 палате', ''],
        ['Операция ЪУЪ', 'Комедии'],
        ['Задачник по албанскому мату с решениями', 'Мультфильмы'],
        ['Как править миром незаметно от санитаров', 'Детективы'],
        ['101 рецепт жарки мяса в ядерном реакторе', 'Ужасы'],
        ['99 способов тушения жажды при помощи скипидара', 'Комедии'],
        ['Кардинал Ришелье и три гвардейца', 'Любовные романы']
    ]

    @pytest.mark.parametrize('name, genre', eight_books_with_genre)
    def test_set_book_genre_eight_books_received_five_genres(self, name, genre):
        collector = BooksCollector()
        for name in range(0, len(self.eight_books_with_genre)):
            collector.add_new_book(self.eight_books_with_genre[name][0])
            collector.set_book_genre(self.eight_books_with_genre[name][0], self.eight_books_with_genre[name][1])
        assert list(collector.get_books_genre().values()) == [
            'Фантастика',
            '',
            'Комедии',
            'Мультфильмы',
            'Детективы',
            'Ужасы',
            ''
        ]

    # 3. Тест для метода get_book_genre - параметризация с фикстурой

    # Cписок для проверки метода - 6 книг с валидными названиями, у одной из книг нет жанра
    books_with_genre = [
        ['Смерть на ЗиЛе', 'Фантастика'],
        ['Как победить при Бородино в 6 палате', ''],
        ['Операция ЪУЪ', 'Комедии'],
        ['Задачник по албанскому мату с решениями', 'Мультфильмы'],
        ['Как править миром незаметно от санитаров', 'Детективы'],
        ['101 рецепт жарки мяса в ядерном реакторе', 'Ужасы']
    ]

    @pytest.mark.parametrize('name, genre', books_with_genre)
    def test_get_book_genre_six_books_five_genres(self, books_collector, name, genre):
        assert books_collector.get_book_genre(name) == genre

    # 4. Тест для метода get_books_with_specific_genre - в запросе валидный жанр - с фикстурой
    def test_get_books_with_specific_genre_valid_genre_book_received(self, books_collector):
        assert books_collector.get_books_with_specific_genre('Комедии') == ['Операция ЪУЪ']

    # 5. Тест для метода get_books_with_specific_genre - в запросе нет жанра - с фикстурой
    def test_get_books_with_specific_genre_no_genre_no_book_received(self, books_collector):
        assert books_collector.get_books_with_specific_genre('') == []

    # 6. Тест для метода get_books_genre - с фикстурой
    def test_get_books_genre_six_books_received_dictionary(self, books_collector):
        assert books_collector.get_books_genre() == {
            'Смерть на ЗиЛе': 'Фантастика',
            'Как победить при Бородино в 6 палате': '',
            'Операция ЪУЪ': 'Комедии',
            'Задачник по албанскому мату с решениями': 'Мультфильмы',
            'Как править миром незаметно от санитаров': 'Детективы',
            '101 рецепт жарки мяса в ядерном реакторе': 'Ужасы'
        }

    # 7. Тест для метода get_books_for_children - с фикстурой
    def test_get_books_for_children_six_books_received_three_books(self, books_collector):
        assert books_collector.get_books_for_children() == [
            'Смерть на ЗиЛе',
            'Операция ЪУЪ',
            'Задачник по албанскому мату с решениями'
        ]

    # 8. Тест для метода add_book_in_favorites - параметризация с фикстурой
    def test_add_book_in_favorites_three_books_received_one(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        # Повторяем ввод, чтобы проверить что одну и ту же книгу нельзя повторно добавить в Избранное
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        # Проверяем, что новую книгу нельзя добавить в Избранное, если ее нет в списке книг
        books_collector.add_book_in_favorites('Жизнь прекрасна')
        assert books_collector.get_list_of_favorites_books() == ['Смерть на ЗиЛе']

    # 9. Тест для метода delete_book_from_favorites - с фикстурой
    def test_delete_book_from_favorites_one_book_deleted_empty_list(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        books_collector.delete_book_from_favorites('Смерть на ЗиЛе')
        assert books_collector.get_list_of_favorites_books() == []

    # 10. Тест для метода get_list_of_favorites_books - с фикстурой
    def test_get_list_of_favorites_books_one_book_received_list_with_one_book(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        assert books_collector.get_list_of_favorites_books() == ['Смерть на ЗиЛе']
