import pytest

from main import BooksCollector


class TestBooksCollector:

    # 1. Тест для метода add_new_book - валидные книги - параметризация
    # Используем валидные названия книг с длиной в 1, 2, 14, 39 и 40 символов
    book_to_add = [
        'Ъ',
        'ЪУ',
        'Смерть на ЗиЛе',
        'Задачник по албанскому мату с решениями',
        'Как править миром незаметно от санитаров'
    ]

    @pytest.mark.parametrize('name', book_to_add)
    def test_add_new_books_valid_book_one_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    # 2. Тест для метода add_new_book - две одинаковые книги c валидным названием
    def test_add_new_books_two_same_books_one_added(self):
        collector = BooksCollector()
        collector.add_new_book('Смерть на ЗиЛе')
        collector.add_new_book('Смерть на ЗиЛе')
        assert len(collector.get_books_genre()) == 1

    # 3. Тест для метода add_new_book - невалидные книги - параметризация
    # Используем невалидные названия книг с длиной в 0, 41 и 46 символов
    book_to_add = [
        '',
        '99 рецептов жарки мяса в ядерном реакторе',
        'Самоучитель по игре на воображаемом контрабасе'
    ]

    @pytest.mark.parametrize('name', book_to_add)
    def test_add_new_books_invalid_book_no_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # 4. Тест для метода set_book_genre - параметризация
    # Cписок для проверки метода - 2 книги с валидными названиями, у одной из которых нет жанра,
    books_with_genre = [
        ['Смерть на ЗиЛе', 'Фантастика'],
        ['Как победить при Бородино в 6 палате', ''],
    ]

    @pytest.mark.parametrize('name, genre', books_with_genre)
    def test_set_book_genre_two_books_received_one_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert list(collector.get_books_genre().values()) == [genre]

    # 5. Тест для метода get_book_genre
    def test_get_book_genre_one_book_received_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Операция ЪУЪ')
        collector.set_book_genre('Операция ЪУЪ', 'Комедии')
        assert collector.get_book_genre('Операция ЪУЪ') == 'Комедии'

    # 6. Тест для метода get_books_with_specific_genre - в запросе валидный жанр - с фикстурой
    def test_get_books_with_specific_genre_valid_genre_book_received(self, books_collector):
        assert books_collector.get_books_with_specific_genre('Фантастика') == ['Смерть на ЗиЛе']

    # 7. Тест для метода get_books_with_specific_genre - в запросе нет жанра - с фикстурой
    def test_get_books_with_specific_genre_no_genre_no_book_received(self, books_collector):
        assert books_collector.get_books_with_specific_genre('') == []

    # 8. Тест для метода get_books_genre - с фикстурой
    def test_get_books_genre_two_books_received_dictionary(self, books_collector):
        assert books_collector.get_books_genre() == {
            'Смерть на ЗиЛе': 'Фантастика',
            'Как править миром незаметно от санитаров': 'Детективы',
        }

    # 9. Тест для метода get_books_for_children - с фикстурой
    def test_get_books_for_children_two_books_received_one_book(self, books_collector):
        assert books_collector.get_books_for_children() == [
            'Смерть на ЗиЛе'
        ]

    # 10. Тест для метода add_book_in_favorites - с фикстурой
    def test_add_book_in_favorites_one_book_received_one(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        assert books_collector.get_list_of_favorites_books() == ['Смерть на ЗиЛе']

    # 11. Тест для метода add_book_in_favorites - с фикстурой -
    # Проверяем, что новую книгу нельзя добавить в Избранное, если ее нет в списке книг
    def test_add_book_in_favorites_new_book_no_book_added(self, books_collector):
        books_collector.add_book_in_favorites('Жизнь прекрасна')
        assert books_collector.get_list_of_favorites_books() == []

    # 12. Тест для метода add_book_in_favorites - с фикстурой
    # Проверяем, что одну и ту же книгу нельзя повторно добавить в Избранное
    def test_add_book_in_favorites_repeat_books_received_one(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        assert books_collector.get_list_of_favorites_books() == ['Смерть на ЗиЛе']

    # 13. Тест для метода delete_book_from_favorites - с фикстурой
    def test_delete_book_from_favorites_one_book_deleted_empty_list(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        books_collector.delete_book_from_favorites('Смерть на ЗиЛе')
        assert books_collector.get_list_of_favorites_books() == []

    # 14. Тест для метода get_list_of_favorites_books - с фикстурой
    def test_get_list_of_favorites_books_one_book_received_list_with_one_book(self, books_collector):
        books_collector.add_book_in_favorites('Смерть на ЗиЛе')
        assert books_collector.get_list_of_favorites_books() == ['Смерть на ЗиЛе']
