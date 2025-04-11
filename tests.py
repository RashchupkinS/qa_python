import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Список названий книг для тестирования
    books = [
        'Гордость и предубеждение и зомби',
        'Что делать, если ваш кот хочет вас убить',
        'Зомби апокалипсис'
    ]

    # Список названий книг с жанрами для тестирования
    books_with_genre = [
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
        ['Зомби апокалипсис', 'Ужасы']
    ]

    # Тест добавления двух новых книг в коллекцию
    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2


    # Тест устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre
    @pytest.mark.parametrize("book_title, genre", books_with_genre)
    def test_set_book_genre_add_book_with_genre(self, collector, book_title, genre):

        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert collector.books_genre[book_title] == genre

    # Тест выводит жанр книги по её имени
    @pytest.mark.parametrize("book_title, genre", books_with_genre)
    def test_get_book_genre_add_book_with_genre(self, collector, book_title, genre):

        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert collector.get_book_genre(book_title) == genre


    # Тест выводит список книг с определённым жанром
    def test_get_books_with_specific_genre_add_two_books_with_the_same_genre(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Зомби апокалипсис')
        collector.set_book_genre('Зомби апокалипсис', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    # Тест выводит текущий словарь books_genre
    def test_get_books_genre_add_two_books_to_the_dictionary(self, collector):

        collector.add_new_book('Маска')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Маска': '',
                                         'Гордость и предубеждение и зомби': ''}

    # Тест возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
    def test_get_books_for_children_add_book_with_genre_for_children_to_list(self, collector):

        collector.add_new_book('Ну, погоди!')
        collector.set_book_genre('Ну, погоди!', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_for_children() == ['Ну, погоди!']

    #  Тест добавляет книгу в избранное. Книга должна находиться в словаре books_genre
    @pytest.mark.parametrize("book_title", books)
    def test_add_book_in_favorites_add_book_to_the_dictionary_of_the_books_genre(self, collector, book_title):

        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)
        assert book_title in collector.favorites

    # Тест проверяет невозможность добавления книги в список избранное, если книга там уже есть
    @pytest.mark.parametrize("book_title", books)
    def test_add_book_in_favorites_duplicate_book_is_not_been_added_to_the_dictionary_of_books_genre(self, collector, book_title):

        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)
        collector.add_book_in_favorites(book_title)
        assert len(collector.favorites) == 1

    # Тест удаления книги из избранного
    @pytest.mark.parametrize("book_title", books)
    def test_delete_book_from_favorites_add_and_delete_book_from_the_list_of_favorites(self, collector, book_title):

        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)
        collector.delete_book_from_favorites(book_title)
        assert book_title not in collector.favorites

    # Тест получения списка избранных книг
    @pytest.mark.parametrize("book_title", books)
    def test_get_list_of_favorites_books_add_book_to_the_list_of_favorites(self, collector, book_title):

        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)
        assert collector.get_list_of_favorites_books() == [book_title]






