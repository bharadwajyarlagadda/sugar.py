# -*- coding: utf-8 -*-

from .fixtures import parametrize

from sugar import construct


def double(variable):
    """Returns twice of a variable."""
    return variable * 2


def triple(variable):
    """Returns thrice of a variable."""
    return variable * 3


@parametrize('length,method,expected_output', [
    (4, double, [0, 2, 4, 6]),
    (4, triple, [0, 3, 6, 9])
])
def test_construct(length, method, expected_output):
    """Tests whether the construct method is working properly or not."""
    assert construct(length, method) == expected_output
