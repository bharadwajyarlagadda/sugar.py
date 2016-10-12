# -*- coding: utf-8 -*-

from .fixtures import parametrize

from sugar import (
    average,
    clone,
    compact,
    construct,
    count,
    every,
    exclude,
    filter,
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


@parametrize('array,expected_output', [
    ([1, 2, 3], [1, 2, 3])
])
def test_clone(array, expected_output):
    """Tests whether the clone method is working properly or not."""
    assert clone(array) == expected_output


@parametrize('array,all,expected_output', [
    ([1, None, '', 2], False, [1, '', 2]),
    ([1, None, '', False, 2], True, [1, 2])
])
def test_compact(array, all, expected_output):
    """Tests whether the compact method is working properly or not."""
    assert compact(array, all) == expected_output


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


@parametrize('array,value,expected_output', [
    ([2, 2, 2], 2, True),
    ([2, 3, 4], 2, False)
])
def test_every(array, value, expected_output):
    """Tests whether the every method is working properly or not."""
    assert every(array, value) == expected_output


@parametrize('array,item,expected_output', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], 4, [1, 2, 3])
])
def test_exclude(array, item, expected_output):
    """Tests whether the exclude method is working properly or not."""
    assert exclude(array, item) == expected_output


@parametrize('array,value,callback,expected_output', [
    ([1, 2, 2, 4], 2, None, [2, 2]),
    ([1, 2, 3, 3, 4], None, lambda x: x > 1, [2, 3, 3, 4])
])
def test_filter(array, value, callback, expected_output):
    """Tests whether the filter method is working properly or not."""
    assert filter(array, value, callback) == expected_output


@parametrize('array,item,expected_output', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], [4], [1, 2, 3])
])
def test_subtract(array, item, expected_output):
    """Tests whether the subtract method is working properly or not."""
    assert subtract(array, item) == expected_output
