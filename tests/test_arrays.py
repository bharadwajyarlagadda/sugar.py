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
    assert _.average(array) == expected_average


@parametrize('array,expected', [
    ([1, 2, 3], [1, 2, 3])
])
def test_clone(array, expected):
    assert _.clone(array) == expected


@parametrize('array,all,expected', [
    ([1, None, '', 2], False, [1, '', 2]),
    ([1, None, '', False, 2], True, [1, 2])
])
def test_compact(array, all, expected):
    assert _.compact(array, all) == expected


@parametrize('length,callback,expected', [
    (4, double, [0, 2, 4, 6]),
    (4, triple, [0, 3, 6, 9])
])
def test_construct(length, callback, expected):
    assert _.construct(length, callback) == expected


@parametrize('array,value,expected', [
    ([1, 2, 3, 3, 4], 3, 2),
    ([1, 2, 3, 3, 4], 5, 0)
])
def test_count(array, value, expected):
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
    assert _.every(array, value) == expected


@parametrize('array,item,expected', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], 4, [1, 2, 3])
])
def test_exclude(array, item, expected):
    assert _.exclude(array, item) == expected


@parametrize('array,value,callback,expected', [
    ([1, 2, 2, 4], 2, None, [2, 2]),
    ([1, 2, 3, 3, 4], None, lambda x: x > 1, [2, 3, 3, 4])
])
def test_filter(array, value, callback, expected):
    assert _.filter_(array, value, callback) == expected


@parametrize('array,num,expected', [
    ([11, 22, 33, 44], 1, [11]),
    ([11, 22, 33, 44], None, []),
    ([11, 22, 33, 44], -3, []),
    ([11, 22, 33, 44], 9, [11, 22, 33, 44])
])
def test_first(array, num, expected):
    assert _.first(array, num) == expected


@parametrize('array,index,expected', [
    ([11, 22, 33], 1, [22, 33]),
    ([11, 22, 33], 2, [33]),
    ([11, 22, 33], None, [11, 22, 33])
])
def test_from(array, index, expected):
    assert _.from_(array, index) == expected


@parametrize('array,search,fromindex,expected', [
    ([11, 22, 33], 22, 1, True),
    ([11, 22, 33], 22, 2, False),
    ([11, 22, 33], 33, None, True),
    ([11, 22, 33], 22, 0, True),
    ([11, 22, 33], 55, None, False),
    ([11, 22, 33], 33, -1, True)
])
def test_includes(array, search, fromindex, expected):
    assert _.includes(array, search, fromindex) == expected


@parametrize('array,expected', [
    ([], True),
    ([None], False),
    ([1, 2], False)
])
def test_is_empty(array, expected):
    assert _.is_empty(array) == expected


@parametrize('array_one,array_two,expected', [
    ([1, 2], [1, 2], True),
    ([1, 2], [2, 1], False),
    ([], [], True),
    ([None], [], False),
    (['1'], [str(1)], True)
])
def test_is_equal(array_one, array_two, expected):
    assert _.is_equal(array_one, array_two) == expected


@parametrize('array,num,expected', [
    ([11, 22, 33, 44], 1, [44]),
    ([11, 22, 33, 44], None, []),
    ([11, 22, 33, 44], -3, []),
    ([11, 22, 33, 44], 9, []),
    ([11, 22, 33, 44], 3, [22, 33, 44])
])
def test_last(array, num, expected):
    assert _.last(array, num) == expected


@parametrize('array,value,callback,expected', [
    ([2, 2, 2], 2, None, True),
    ([2, 3, 4], 2, None, True),
    ([1, 2, 3, 4], 5, None, False),
    (['a', 'b', 'c'], 'a', None, True),
    (['a', 'b', 'c'], None, lambda x: x == 'c', True)
])
def test_some(array, value, callback, expected):
    assert _.some(array, value, callback) == expected


@parametrize('array,item,expected', [
    ([1, 2, 3], 3, [1, 2]),
    ([1, 2, 3], [1, 3], [2]),
    ([1, 2, 3], [4], [1, 2, 3])
])
def test_subtract(array, item, expected):
    assert _.subtract(array, item) == expected


@parametrize('array,other,expected', [
    ([1, 2, 3], [2, 3, 4], [1, 2, 3, 4]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    (['a', 'b', 'c'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd'])
])
def test_union(array, other, expected):
    assert _.union(array, other) == expected
