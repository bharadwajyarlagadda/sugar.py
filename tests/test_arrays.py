# -*- coding: utf-8 -*-

from .fixtures import parametrize

import sugar as _


def double(variable):
    """Returns twice of a variable."""
    return variable * 2


def triple(variable):
    """Returns thrice of a variable."""
    return variable * 3


@parametrize('array,item,index,expected', [
    ([11, 22, 33], 44, None, [11, 22, 33, 44]),
    ([11, 22, 33], 44, 1, [11, 44, 22, 33]),
    ([11, 22, 33], [44, 55], None, [11, 22, 33, 44, 55]),
    ([11, 22, 33], [44, 55], 1, [11, 44, 55, 22, 33]),
    ([11, 22, 33], {'a': 1}, 1, [11, {'a': 1}, 22, 33]),
    ([11, 22, 33], [{'a': 1}, {'b': 2}], 1, [11, {'a': 1}, {'b': 2}, 22, 33]),
    ([11, 22, 33], 'abcd', None, [11, 22, 33, 'abcd']),
    ([11, 22, 33], None, 1, [11, 22, 33])
])
def test_add(array, item, index, expected):
    assert _.add(array, item, index) == expected


@parametrize('array,item,index,expected', [
    ([11, 22, 33], 44, None, [11, 22, 33, 44]),
    ([11, 22, 33], 44, 1, [11, 44, 22, 33]),
    ([11, 22, 33], [44, 55], None, [11, 22, 33, 44, 55]),
    ([11, 22, 33], [44, 55], 1, [11, 44, 55, 22, 33]),
    ([11, 22, 33], {'a': 1}, 1, [11, {'a': 1}, 22, 33]),
    ([11, 22, 33], [{'a': 1}, {'b': 2}], 1, [11, {'a': 1}, {'b': 2}, 22, 33]),
    ([11, 22, 33], 'abcd', None, [11, 22, 33, 'abcd']),
    ([11, 22, 33], None, 1, [11, 22, 33])
])
def test_append(array, item, index, expected):
    assert _.append(array, item, index) == expected


@parametrize('array,expected_average', [
    ([1, 2, 3], 2)
])
def test_average(array, expected_average):
    """Tests whether the average method is working properly or not."""
    assert _.average(array) == expected_average


@parametrize('array,expected', [
    ([1, 2, 3], [1, 2, 3])
])
def test_clone(array, expected):
    """Tests whether the clone method is working properly or not."""
    assert _.clone(array) == expected


@parametrize('array,all,expected', [
    ([1, None, '', 2], False, [1, '', 2]),
    ([1, None, '', False, 2], True, [1, 2])
])
def test_compact(array, all, expected):
    """Tests whether the compact method is working properly or not."""
    assert _.compact(array, all) == expected


@parametrize('length,callback,expected', [
    (4, double, [0, 2, 4, 6]),
    (4, triple, [0, 3, 6, 9])
])
def test_construct(length, callback, expected):
    """Tests whether the construct method is working properly or not."""
    assert _.construct(length, callback) == expected


@parametrize('array,value,expected', [
    ([1, 2, 3, 3, 4], 3, 2),
    ([1, 2, 3, 3, 4], 5, 0)
])
def test_count(array, value, expected):
    """Tests whether the count method is working properly or not."""
    assert _.count(array, value) == expected


@parametrize('obj,copy,expected', [
    ('abc def 10;/',
     True,
     ['a', 'b', 'c', ' ', 'd', 'e', 'f', ' ', '1', '0', ';', '/']),
    (True, False, [True]),
    (1234, True, [1234]),
    (None, True, []),
    ([11, 22, 33, 44], False, [11, 22, 33, 44])
])
def test_create(obj, copy, expected):
    assert _.create(obj, copy) == expected


@parametrize('array,value,expected', [
    ([2, 2, 2], 2, True),
    ([2, 3, 4], 2, False)
])
def test_every(array, value, expected):
    """Tests whether the every method is working properly or not."""
    assert _.every(array, value) == expected


@parametrize('array,item,expected', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], 4, [1, 2, 3])
])
def test_exclude(array, item, expected):
    """Tests whether the exclude method is working properly or not."""
    assert _.exclude(array, item) == expected


@parametrize('array,value,callback,expected', [
    ([1, 2, 2, 4], 2, None, [2, 2]),
    ([1, 2, 3, 3, 4], None, lambda x: x > 1, [2, 3, 3, 4])
])
def test_filter(array, value, callback, expected):
    """Tests whether the filter method is working properly or not."""
    assert _.filter(array, value, callback) == expected


@parametrize('array,item,expected', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], [4], [1, 2, 3])
])
def test_subtract(array, item, expected):
    """Tests whether the subtract method is working properly or not."""
    assert _.subtract(array, item) == expected
