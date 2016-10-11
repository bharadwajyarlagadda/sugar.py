# -*- coding: utf-8 -*-

from __future__ import absolute_import


def average(array):
    """Returns the average for all the values in the given :attr:`array`.

    Args:
        array (list): List of values.

    Returns:
        int/float: Average of all the values in the given list.

    Example:

        >>> float(average([1, 2, 3]))
        2.0

    .. versionadded:: 0.1.0
    """
    return sum(array) / len(array)


def construct(var, callback):
    """Constructs an array of :attr:`var` length from the values of
    :attr:`callback`.

    Args:
        var (int): Length of the array intended.
        callback: A method that can take in each variable from the given range
            and return back a new value based on the method definition.

    Returns:
        list: A list of :attr:`callback` values.

    Example:

        >>> construct(4, lambda x: x * 2)
        [0, 2, 4, 6]

    .. versionadded:: 0.1.0
    """
    return [callback(i) for i in range(0, var)]


def count(array, value):
    """Counts all elements in the :attr:`array` that match the given
    :attr:`value`.

    Args:
        array (list): A list of values provided by the user to search for.
        value (int/float/str): Value that needs to be counted.

    Returns:
        int: Count of the given value.

    Example:

        >>> count([1, 2, 3, 3], 3)
        2

    .. versionadded:: 0.1.0
    """
    return array.count(value)


def subtract(array, item):
    """Subtracts :attr:`item` from the :attr:`array` and returns the result
    as a new array. If :attr:`item` is also an array, all elements in it will
    be removed.

    Args:
        array (list): A list of values provided by the user.
        item (list/int/float/str): A value that needs to be removed from
            :attr:`array`.

    Returns:
        list: A new list with the :attr:`item` removed.

    Example:

        >>> subtract([1, 2, 3], 2)
        [1, 3]
        >>> subtract ([1, 2, 3], [1, 3])
        [2]
        >>> subtract([1, 2, 3], 4)
        [1, 2, 3]

    .. versionadded:: 0.1.0
    """
    if not isinstance(item, list):
        # If item is not a list, convert it into list.
        item = [item]

    return [element for element in array if element not in item]
