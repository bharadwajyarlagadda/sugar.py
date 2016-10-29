# -*- coding: utf-8 -*-

from .fixtures import parametrize

import sugar as _


@parametrize('case,expected', [
    ((0, 999), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
])
def test_armstrongs_between(case, expected):
    assert _.armstrongs_between(*case) == expected


@parametrize('num,expected', [
    (371, True),
    (8208, True),
    (51, False)
])
def test_is_armstrong(num, expected):
    assert _.is_armstrong(num) == expected


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


@parametrize('num,expected', [
    (13, True),
    (727021, True),
    (10, False),
    (21, False),
    (37, True)
])
def test_is_prime(num, expected):
    assert _.is_prime(num) == expected


@parametrize('case,expected', [
    ((1, 20), [1, 2, 3, 5, 7, 11, 13, 17, 19]),
    ((21, 40), [23, 29, 31, 37])
])
def test_primes_between(case, expected):
    assert _.primes_between(*case) == expected


@parametrize('args', [
    (0, 5),
    (2, 5),
    (-6, 0),
    (5.5, 11.7),
    (5.5, 6.5)
])
def test_random(args):
    assert args[0] <= _.random_(*args) <= args[1]
