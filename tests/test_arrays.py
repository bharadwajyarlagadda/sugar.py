# -*- coding: utf-8 -*-

from .fixtures import parametrize

from sugar import (
    average,
    construct,
    count,
    subtract
)


def double(variable):
    """Returns twice of a variable."""
    return variable * 2


def triple(variable):
    """Returns thrice of a variable."""
    return variable * 3


@parametrize('array,expected_average', [
    ([1, 2, 3], 2)
])
def test_average(array, expected_average):
    """Tests whether the average method is working properly or not."""
    assert average(array) == expected_average


@parametrize('length,callback,expected_output', [
    (4, double, [0, 2, 4, 6]),
    (4, triple, [0, 3, 6, 9])
])
def test_construct(length, callback, expected_output):
    """Tests whether the construct method is working properly or not."""
    assert construct(length, callback) == expected_output


@parametrize('array,value,expected_output', [
    ([1, 2, 3, 3, 4], 3, 2),
    ([1, 2, 3, 3, 4], 5, 0)
])
def test_count(array, value, expected_output):
    """Tests whether the count method is working properly or not."""
    assert count(array, value) == expected_output


@parametrize('array,item,expected_output', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], [4], [1, 2, 3])
])
def test_subtract(array, item, expected_output):
    """Tests whether the subtract method is working properly or not."""
    assert subtract(array, item) == expected_output
