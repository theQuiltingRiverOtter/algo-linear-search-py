from linear_search import linear_search, linear_search_global
import pytest


# tests for linear search with array of numbers
def test_linear_search_exists():
    assert linear_search(3, [1, 2, 3, 3]) == 2


def test_linear_search_does_not_exist():
    assert linear_search(4, [1, 2, 3]) == None


def test_linear_search_each_int_exists_but_not_whole():
    assert linear_search(13, [1, 4, 2, 3]) == None


# tests for linear search with string and single character
def test_linear_search_exists_string():
    assert linear_search("l", "hello world") == 2


def test_linear_search_does_not_exist_string():
    assert linear_search("z", "hello world") == None


# tests for linear search with tuple
def test_linear_search_exists_tuple():
    assert linear_search(4, (4, 5, 6)) == 0


def test_linear_search_does_not_exist_tuple():
    assert linear_search(7, (4, 5, 6)) == None


# tests for linear_search_global with array of numbers
def test_global_search_multiple_numbers():
    assert linear_search_global(3, [2, 8, 1, 3, 5, 8, 12, 23, 3, 24, 100, 3]) == [
        3,
        8,
        11,
    ]


def test_global_search_single_number():
    assert linear_search_global(8, [2, 8, 1, 3, 5, 8, 12, 23, 3, 24, 100, 3]) == [1]


def test_global_search_number_does_not_exist():
    assert linear_search_global(4, [2, 8, 1, 3, 5, 8, 12, 23, 3, 24, 100, 3]) == []


# tests for linear_search_global
def test_global_search_multiple_chars():
    assert linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]


def test_global_search_single_char():
    assert linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6]


def test_global_search_duplicate_char():
    assert linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4]


# tests for linear_search_global with tuple
def test_global_search_multiple_numbers_tuple():
    assert linear_search_global(
        12, (1, 3, 8, 12, 4, 16, 18, 12, 21, 53, 55, 12, 332)
    ) == [3, 7, 11]


def test_global_search_single_number():
    assert linear_search_global(
        8, (1, 3, 8, 12, 4, 16, 18, 12, 21, 53, 55, 12, 332)
    ) == [2]


def test_global_search_does_not_exist_tuple():
    assert (
        linear_search_global(2, (1, 3, 8, 12, 4, 16, 18, 12, 21, 53, 55, 12, 332)) == []
    )
