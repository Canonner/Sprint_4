## Финальный проект 4 спринта

Файл tests.py содержит юнит-тесты для проверки методов класса BooksCollector,
находящихся в файле main.py

### Фикстура books_collector

Для уменьшения количества строк кода используется фикстура
books_collector, которая:
- создает экземпляр класса BooksCollector
- используя цикл, заполняет список books_genre названиями книг и их жанрами
- возвращает экземпляр

Используется минимально возможное количество книг - 2
 
Фикстура находится в файле conftest.py

### Список тестов

1.  Тест для метода add_new_book - в запросе валидные названия: test_add_new_books_valid_book_one_added.
2.  Тест для метода add_new_book - в запросе два одинаковых названия: test_add_new_books_two_same_books_one_added
3.  Тест для метода add_new_book - в запросе невалидные названия: test_add_new_books_invalid_book_no_book_added
4.  Тест для метода set_book_genre: test_set_book_genre_two_books_received_one_genre
5.  Тест для метода get_book_genre: test_get_book_genre_one_book_received_genre
6.  Тест для метода get_books_with_specific_genre - в запросе валидный жанр: test_get_books_with_specific_genre_valid_genre_book_received
7.  Тест для метода get_books_with_specific_genre - в запросе нет жанра: test_get_books_with_specific_genre_no_genre_no_book_received
8.  Тест для метода get_books_genre: test_get_books_genre_two_books_received_dictionary
9.  Тест для метода get_books_for_children: test_get_books_for_children_two_books_received_one_book
10. Тест для метода add_book_in_favorites - в запросе одна книга: test_add_book_in_favorites_two_books_received_one
11. Тест для метода add_book_in_favorites - в запросе новая книга: test_add_book_in_favorites_new_book_no_book_added
12. Тест для метода add_book_in_favorites - в запросе два одинаковых названия: test_add_book_in_favorites_repeat_books_received_one
13. Тест для метода delete_book_from_favorites: test_delete_book_from_favorites_one_book_deleted_empty_list
14. Тест для метода get_list_of_favorites_books: test_get_list_of_favorites_books_one_book_received_list_with_one_book


