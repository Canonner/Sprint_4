</h2>

<p align="center">

## Финальный проект 4 спринта

Файл tests.py содержит юнит-тесты для проверки методов класса BooksCollector,
находящихся в файле main.py

<p align="center">

### Фикстура books_collector

Для уменьшения количества строк кода используется фикстура
books_collector, которая:
- создает экземпляр класса BooksCollector
- используя цикл, заполняет список books_genre названиями книг и их жанрами
- возвращает экземпляр
 
Фикстура находится в файле conftest.py

### Список тестов

1.  Тест для метода add_new_book: test_add_new_book_seven_books_four_added
2.  Тест для метода set_book_genre: test_set_book_genre_eight_books_received_five_genres
3.  Тест для метода get_book_genre: test_get_book_genre_six_books_five_genres
4.  Тест для метода get_books_with_specific_genre - в запросе валидный жанр: test_get_books_with_specific_genre_valid_genre_book_received
5.  Тест для метода get_books_with_specific_genre - в запросе нет жанра: test_get_books_with_specific_genre_no_genre_no_book_received
6.  Тест для метода get_books_genre: test_get_books_genre_six_books_received_dictionary
7.  Тест для метода get_books_for_children: test_get_books_for_children_six_books_received_three_books
8.  Тест для метода add_book_in_favorites: test_add_book_in_favorites_three_books_received_one
9.  Тест для метода delete_book_from_favorites: test_delete_book_from_favorites_one_book_deleted_empty_list
10. Тест для метода get_list_of_favorites_books: test_get_list_of_favorites_books_one_book_received_list_with_one_book


