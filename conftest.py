import pytest
from main import BooksCollector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def add_books():
    collector = BooksCollector()
    collector.add_new_book('Властелин колец')
    collector.add_new_book('Властелин колец две крепости')
    collector.add_new_book('Властелин колец возвращение короля')
    collector.add_new_book('Властелин колец братство кольца')
    collector.set_book_genre('Властелин колец', 'Детективы')
    collector.set_book_genre('Властелин колец две крепости', 'Детективы')
    collector.set_book_genre('Властелин колец возвращение короля', 'Ужасы')
    collector.set_book_genre('Властелин колец братство кольца', 'Мультфильмы')
    return collector
