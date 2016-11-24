# -*- coding: utf-8 -*-

from __future__ import absolute_import

import random
import math

from ._compat import _range


def armstrongs_between(n1=None, n2=None):
    """Get all the armstrong numbers between :attr:`n1` and :attr:`n2`.

    Args:
        n1 (int): Number passed in by the user.
        n2 (int): Number passed in by the user.

    Returns:
        list: List of all the armstrong numbers between :attr:`n1`, and
            :attr:`n2`.

    Example:

        >>> armstrongs_between(0, 999)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

    .. versionadded:: TODO

    .. note:: When you pass in different digit numbers, this method doesn't
        get the armstrong numbers compared to the highest digit number passed
        in.
    """
    n1 = 0 if not n1 else n1
    n2 = 0 if not n2 else n2

    max_value = max(n1, n2)
    min_value = min(n1, n2)

    return [num
            for num in _range(min_value, max_value + 1)
            if is_armstrong(num)]


def hex_(value, pad=None):
    """Converts a given number to hexi-decimal.

    Args:
        value (int): Value passed in by the user.
        pad (int): Padding till the result can be restricted.

    Returns:
        hex: A hex value that corresponds to the given number.

    Example:

        >>> hex_(55)
        '0x37'
        >>> hex_(555)
        '0x22b'
        >>> hex_(555, 2)
        '0x'

    .. versionadded:: TODO
    """
    return hex(value)[0:pad]


def is_armstrong(num):
    """Returns True if :attr:`num` is armstrong number.

    Args:
        num (int): Number passed in by the user.

    Returns:
        bool: True if the given :attr:`num` is armstrong number else False.

    Example:

        >>> is_armstrong(371)
        True
        >>> is_armstrong(8208)
        True
        >>> is_armstrong(51)
        False

    .. versionadded:: TODO
    """
    total = 0
    temp = num
    digits = len(str(num))

    while temp != 0:
        remainder = temp % 10
        total += math.pow(remainder, digits)
        temp //= 10

    if total == num:
        result = True
    else:
        result = False

    return result


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


def is_odd(num):
    """Returns True if :attr:`num` is odd.

    Args:
        num (int/float): Number passed in by the user.

    Returns:
        bool: True if :attr:`num` is odd else False

    Example:

        >>> is_odd(6)
        False
        >>> is_odd(7)
        True

    .. versionadded:: TODO
    """
    return num % 2 != 0


def is_prime(num):
    """Returns True if the give :attr:`num` is a prime number.

    Args:
        num (int/float): Number passed in by the user.

    Returns:
        bool: True if the given :attr:`num` is a prime number else False

    Example:

        >>> is_prime(5)
        True
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
        >>> is_prime(727021)
        True

    .. versionadded:: TODO
    """
    count = 0

    if num in [1, 2]:
        return True

    for i in _range(1, (int(math.ceil(math.sqrt(num))) + 1)):
        if num % i == 0:
            count += 1

    if count <= 1:
        result = True
    else:
        result = False

    return result


def primes_between(n1=None, n2=None):
    """Get all the prime numbers between :attr:`n1` and :attr:`n2`.

    Args:
        n1 (int): Number passed in by the user.
        n2 (int): Number passed in by the user.

    Returns:
        list: List of all the prime numbers between :attr:`n1`, and :attr:`n2`.

    Example:

        >>> primes_between(1, 20)
        [1, 2, 3, 5, 7, 11, 13, 17, 19]
        >>> primes_between(21, 40)
        [23, 29, 31, 37]

    .. versionadded:: TODO
    """
    n1 = 0 if not n1 else n1
    n2 = 0 if not n2 else n2

    max_value = max(n1, n2)
    min_value = min(n1, n2)

    return [num for num in _range(min_value, max_value + 1) if is_prime(num)]


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
