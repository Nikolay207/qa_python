from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_books_genre_empty_at_start(self,collector):
        assert collector.books_genre == {}

    def test_favorites_empty_at_start(self,collector):
        assert collector.favorites == []

    @pytest.mark.parametrize('genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_genre_has_expected_list(self,collector,genre):
        assert genre in collector.genre

    def test_genre_age_rating_has_expected_list(self,collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_success(self,collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Властелин колец две крепости')
        assert collector.get_books_genre() == {'Властелин колец':'','Властелин колец две крепости':''}

    def test_set_book_genre_skips_if_book_missing(self,collector):
        collector.set_book_genre('Властелин колец','Детективы')
        assert 'Властелин колец' not in collector.books_genre

    def test_set_book_genre_success(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Детективы')
        assert collector.books_genre.get('Властелин колец') =='Детективы'

    @pytest.mark.parametrize("name, genre",[('Властелин колец', 'Детективы'),
                              ('Властелин колец возвращение короля', 'Ужасы'),
                              ('Властелин колец братство кольца', 'Мультфильмы')])
    def test_get_book_genre_returns_correct_genre(self,add_books,name,genre):
        result = add_books.get_book_genre(name)
        assert result == genre

    @pytest.mark.parametrize("genre, expected", [('Детективы', ['Властелин колец', 'Властелин колец две крепости']),
                                                 ('Фантастика', []),
                                                 ('Ужасы', ['Властелин колец возвращение короля']),
                                                 ('Мультфильмы',['Властелин колец братство кольца'])])
    def test_get_books_with_specific_genre_works(self,add_books,genre,expected):
        result = add_books.get_books_with_specific_genre(genre)
        assert result == expected

    def test_get_books_for_children_returns_only_children_books(self,add_books):
        result = add_books.get_books_for_children()
        assert result == ['Властелин колец братство кольца']

    @pytest.mark.parametrize('favorites', ['Война и мир', 'Маленький принц', 'Старик и море', '1984'])
    def test_add_book_in_favorites_skips_if_book_missing(self,favorites,add_books):
        add_books.add_book_in_favorites(favorites)
        assert add_books.favorites == []

    def test_add_book_in_favorites_success(self,add_books):
        add_books.add_book_in_favorites('Властелин колец две крепости')
        add_books.add_book_in_favorites('Властелин колец братство кольца')
        assert add_books.favorites == ['Властелин колец две крепости','Властелин колец братство кольца']

    def test_delete_book_from_favorites_success(self, add_books):
        add_books.add_book_in_favorites('Властелин колец две крепости')
        add_books.add_book_in_favorites('Властелин колец братство кольца')
        add_books.delete_book_from_favorites('Властелин колец две крепости')
        assert add_books.get_list_of_favorites_books() == ['Властелин колец братство кольца']
