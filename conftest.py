import pytest
from main import BooksCollector


# Фикстура для создания экземпляра класса BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()