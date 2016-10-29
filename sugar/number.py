# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import random
import math


def is_even(num):
    """Returns True if :attr:`num` is even.

    Args:
        num (int/float): Number passed in by the user.

    Returns:
        bool: True if :attr:`num` is even else False

    Example:

        >>> is_even(6)
        True
        >>> is_even(7)
        False

    .. versionadded:: TODO
    """
    return num % 2 == 0


def is_multiple_of(value, num):
    """Returns true if the :attr:`value` is a multiple of :attr:`num`.

    Args:
        value (int/float): Value provided by the user.
        num (int/float): Value provided by the user.

    Returns:
        bool: True if the :attr:`value` is a multiple of :attr:`num`.

    Example:

        >>> is_multiple_of(6, 2)
        True
        >>> is_multiple_of(5, 2)
        False
        >>> is_multiple_of(1.5, 3)
        False
        >>> is_multiple_of(1.5, 0.5)
        True

    .. versionadded:: TODO
    """
    return value % num == 0


def random_(n1=None, n2=None):
    """Returns a random integer/float from :attr:`n1` to :attr:`n2` (both
    inclusive)

    Args:
        n1 (int/float/str): Value given by the user.
        n2 (int/float/str): Value given by the user.

    Returns:
        int/float: Random integer/float value between :attr:`n1` and
            :attr:`n2`.

    Example:

        >>> result = random_(5, 6)
        >>> assert 5 <= result <= 6
        >>> result = random_(5)
        >>> assert 0 <= result <= 5

    .. versionadded:: TODO
    """
    n1 = 0 if not n1 else n1
    n2 = 0 if not n2 else n2

    n1 = float(n1)
    n2 = float(n2)

    max_value = max(n1, n2)
    min_value = min(n1, n2)
    diff = max_value - min_value

    result = (random.random() * diff) + min_value

    if diff <= 1 or (diff > 1 and math.ceil(result) > max_value):
        return round(result, 2)
    else:
        return math.ceil(result)
