from main import BooksCollector
import pytest


class TestBooksCollector:



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

    def test_get_book_genre_returns_correct_genre(self, add_books):
        assert add_books.get_book_genre('Властелин колец') == 'Детективы' and add_books.get_book_genre('Властелин колец возвращение короля') == 'Ужасы'


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

    @pytest.mark.parametrize("book_to_delete, book_to_keep", [
        ('Властелин колец две крепости', 'Властелин колец братство кольца')
    ])
    def test_delete_book_from_favorites_success(self, collector, book_to_delete, book_to_keep):
        collector.add_new_book(book_to_delete)
        collector.add_new_book(book_to_keep)
        collector.set_book_genre(book_to_delete, 'Детективы')
        collector.set_book_genre(book_to_keep, 'Мультфильмы')
        collector.add_book_in_favorites(book_to_delete)
        collector.add_book_in_favorites(book_to_keep)
        collector.delete_book_from_favorites(book_to_delete)
        assert collector.get_list_of_favorites_books() == [book_to_keep]

    def test_get_books_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_books_genre() == {'Война и мир': 'Фантастика'}

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == ['Война и мир']
