# -*- coding: utf-8 -*-

from __future__ import absolute_import

import copy

import sugar as _


def add(array, item, index=None):
    """Adds item to the array and returns the result as a new array. If item
    is also an array, it will be concatenated instead of inserted. index will
    control where item is added.

    Args:
        array (list): List of values passed in by the user.
        item (mixed): Value to be added to the array (passed in by the user).
        index (int): Position at which the item will be added to the list.

    Returns:
        list: Adds item to the array and returns the result as a new array.

    Example:

        >>> add([11, 22, 33], 88)
        [11, 22, 33, 88]
        >>> add([11, 22, 33], 88, 1)
        [11, 88, 22, 33]
        >>> add([11, 22, 33], [44, 55])
        [11, 22, 33, 44, 55]
        >>> add([11, 22, 33], [44, 55, 66, 77], 1)
        [11, 44, 55, 66, 77, 22, 33]

    .. versionadded:: TODO
    """
    if index:
        if _.is_array(item):
            array[index:index] = item
        elif not _.is_array(item):
            array.insert(index, item)

    if not index:
        if _.is_array(item):
            array += item
        elif not _.is_array(item):
            array.append(item)

    return array


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


def clone(obj):
    """Returns a shallow copy of the given list. This method can also be used
    for othe objects such as int/float/string.

    Args:
        obj (list): List of values provided by the user.

    Returns:
        list: Shallow copy of the given array.

    Example:

        >>> clone([1, 2, 3])
        [1, 2, 3]
        >>> clone('foobar')
        'foobar'
        >>> clone(1234)
        1234

    .. versionadded:: TODO
    """
    return copy.copy(obj)


def compact(array, all=False):
    """Removes all instances of None, False, empty strings. This includes
    None, False, and empty strings.

    Args:
        array (list): List of values provided by the user.
        all (bool): Boolean value to remove all the instances of None, False
            and empty strings.

    Returns:
        list: List of values with all falsy elements removed.

    Example:

        >>> compact([1, None, 2, False, 3])
        [1, 2, False, 3]
        >>> compact([1, None, '', False, 2], all=True)
        [1, 2]

    .. versionadded:: TODO
    """
    if all:
        return subtract(array, [None, False, ''])

    return subtract(array, None)


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


def create(obj=None, copy=False):
    """Creates an array from an unknown object.

    Args:
        obj (mixed): Value passed in by the user.
        copy (bool): If clone is true, the array will be shallow cloned.

    Returns:
        list: Array from the given object.

    Example:

        >>> create('abc def 109;cd')
        ['a', 'b', 'c', ' ', 'd', 'e', 'f', ' ', '1', '0', '9', ';', 'c', 'd']
        >>> create(1234)
        [1234]
        >>> create([11, 22, 33, 44], copy=True)
        [11, 22, 33, 44]
        >>> create(True)
        [True]
        >>> create()
        []

    .. versionadded:: TODO
    """
    result = None

    if not obj:
        result = []

    if _.is_array(obj):
        if copy:
            # Shallow copy of the object.
            result = clone(obj)
        else:
            # Copies the object. This is the fast way to copy the object.
            result = obj[:]

    if _.is_boolean(obj) or _.is_number(obj):
        if copy:
            # Shallow copy of the object.
            result = [clone(obj)]
        else:
            result = [obj]

    if _.is_string(obj):
        if copy:
            # Shallow copy of the object.
            result = [value for value in clone(obj)[:]]
        else:
            result = [value for value in obj[:]]

    return result


def every(array, value):
    """Returns true if search is true for all elements of the array. In other
    words, this method returns True if :attr:`array` contains all the same
    values :attr:`value`.

    Args:
        array (list): List of values provided by the user.
        value (int/float/str): Value that needs to be searched.

    Returns:
        bool: A boolean value based on the :attr:`array` having all the
            values as :attr:`value`.

    Example:

        >>> every([2, 2, 2], 2)
        True
        >>> every([2, 2, 3], 2)
        False

    .. versionadded:: TODO
    """
    return all(element == value for element in array)


def exclude(array, value):
    """Returns a new array with every element that does not match
    :attr:`value`.

    Args:
        array(list): List of values provided by the user.
        value(int/float/str): A value that needs to be excluded.

    Returns:
        list: List excluding the give :attr:`value`.

    Example:

        >>> exclude([11, 22, 33], 22)
        [11, 33]
        >>> exclude([11, 22, 33], 44)
        [11, 22, 33]
        >>> exclude([11, 22, 33], [11, 22])
        [33]

    .. versionadded:: TODO
    """
    return subtract(array, value)


def filter(array, value=None, callback=None):
    """Returns list of elements in the :attr:`array` that match :attr:`value`.
    Also, returns list of elements based on the given callback method.

    Args:
        array (list): List of values provided by the user.
        value (int/float/str): A value that needs to be matched with.
        callback: A method that takes the value, filters the variable based
            on the given condition and returns the filtered value.

    Returns:
        list: List of values that match with the :attr:`value` or the given
            filter.

    Example:

        >>> filter([1, 2, 2, 4], value=2)
        [2, 2]
        >>> filter([1, 2, 2, 4], callback=lambda x: x > 1)
        [2, 2, 4]

    .. versionadded:: TODO
    """
    if value:
        return [element for element in array if element == value]

    return [element for element in array if callback(element) is True]


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
