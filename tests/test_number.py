# -*- coding: utf-8 -*-

from .fixtures import parametrize

import sugar as _


@parametrize('num,expected', [
    (6, True),
    (7, False)
])
def test_is_even(num, expected):
    assert _.is_even(num) == expected


@parametrize('value,num,expected', [
    (4, 2, True),
    (1.5, 0.5, True),
    (5, 2, False)
])
def test_is_multiple_of(value, num, expected):
    assert _.is_multiple_of(value, num) == expected


@parametrize('num,expected', [
    (6, False),
    (7, True)
])
def test_is_odd(num, expected):
    assert _.is_odd(num) == expected


@parametrize('args', [
    (0, 5),
    (2, 5),
    (-6, 0),
    (5.5, 11.7),
    (5.5, 6.5)
])
def test_random(args):
    assert args[0] <= _.random_(*args) <= args[1]
