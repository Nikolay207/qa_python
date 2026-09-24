# Тесты для класса BooksCollector

## Список тестов:

### Проверка инициализации
- `test_books_genre_empty_at_start` — проверяю что словарь книг пуст при создании
- `test_favorites_empty_at_start` — проверяю что список избранных пуст при создании
- `test_genre_has_expected_list` — проверяю что список жанров содержит все 5 жанров
- `test_genre_age_rating_has_expected_list` — проверяю что список жанров с рейтингом содержит "Ужасы" и "Детективы"

### add_new_book
- `test_add_new_book_success` — проверка успеншного добавления книги

### set_book_genre
- `test_set_book_genre_success` — проверка, что жанр присваивается книги 
- `test_set_book_genre_skips_if_book_missing` — проверка, что жанр не устанавливается если книги нет

### get_book_genre
- `test_get_book_genre_returns_correct_genre` — проверяю что возвращается правильный жанр книги

### get_books_with_specific_genre
- `test_get_books_with_specific_genre_works` — проверяю что возвращается список книг с указанным жанром

### get_books_for_children
- `test_get_books_for_children_returns_only_children_books` — проверяю что возвращаются только детские книги
### add_book_in_favorites
- `test_add_book_in_favorites_success` — проверка, что книга успешно добавляется в избранное
- `test_add_book_in_favorites_skips_if_book_missing` — проверка, что книга не добавляется если её нет в словаре books_genre

### delete_book_from_favorites
- `test_delete_book_from_favorites_success` — проверка, что книга успешно удаляется из избранного