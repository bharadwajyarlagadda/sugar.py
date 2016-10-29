# -*- coding: utf-8 -*-

from __future__ import absolute_import

import copy

from ._compat import _range

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
    return array_append(array, item, index)


def append(array, item, index=None):
    """Appends item to the array. If item is also an array, it will be
    concatenated instead of inserted.

    Args:
        array (list): List of values passed in by the user.
        item (mixed): Value to be added to the array (passed in by the user).
        index (int): Position at which the item will be added to the list.

    Returns:
        list: Appends item to the array and returns the result.

    Example:

        >>> append([11, 22, 33], 88)
        [11, 22, 33, 88]
        >>> append([11, 22, 33], 88, 1)
        [11, 88, 22, 33]
        >>> append([11, 22, 33], [44, 55])
        [11, 22, 33, 44, 55]
        >>> append([11, 22, 33], [44, 55, 66, 77], 1)
        [11, 44, 55, 66, 77, 22, 33]

    .. versionadded:: TODO
    """
    return array_append(array, item, index)


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
    return [callback(i) for i in _range(0, var)]


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


def filter_(array, value=None, callback=None):
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

        >>> filter_([1, 2, 2, 4], value=2)
        [2, 2]
        >>> filter_([1, 2, 2, 4], callback=lambda x: x > 1)
        [2, 2, 4]

    .. versionadded:: TODO
    """
    if value:
        return [element for element in array if element == value]

    return [element for element in array if callback(element) is True]


def first(array, num=1):
    """Returns the first element(s) in the array. When num is passed, returns
    the first num elements in the array.

    Args:
        array (list): List of values passed in by the user.
        num (int): Number passed in by the user.

    Returns:
        list: Returns an array of first :attr:`num` elements.

    Example:

        >>> first([11, 22, 33, 44], 1)
        [11]
        >>> first([11, 22, 33, 44], None)
        []
        >>> first([11, 22, 33, 44], -3)
        []
        >>> first([11, 22, 33, 44], 9)
        [11, 22, 33, 44]

    .. versionadded:: TODO
    """
    num = 0 if (not num or num < 0) else num

    return array[0:num]


def from_(array, index=0):
    """Returns a slice of the array from :attr:`index`.

    Args:
        array (list): A list of values provided by the user.
        index (int): Start position of the array where the slice starts.

    Returns:
        list: Array sliced from :attr:`index`).

    Example:

        >>> from_([11, 22, 33], 1)
        [22, 33]
        >>> from_([11, 22, 33])
        [11, 22, 33]
        >>> from_([11, 22, 33], 2)
        [33]
        >>> from_([11, 22, 33], None)
        [11, 22, 33]

    .. versionadded:: TODO
    """
    return array[index:]


def includes(array, search, fromindex=0):
    """Returns true if search is contained within the array. Search begins at
    fromindex, which defaults to the beginning of the array.

    Args:
        array (list): A list of values provided by the user.
        search (mixed): A value that needs to be searched (provided by the
            user).
        fromindex (int): Search begins at fromindex.

    Returns:
        bool: True if search is contained within the array beginning at
            fromindex position else False.

    Example:

        >>> includes([11, 22, 33], 22, 0)
        True
        >>> includes([11, 22, 33], 22, 1)
        True
        >>> includes([11, 22, 33], 22, 2)
        False
        >>> includes([11, 22, 33], 11, None)
        True
        >>> includes([11, 22, 33], 33)
        True
        >>> includes([11, 22, 33], 22, -1)
        False
        >>> includes([11, 22, 33], 22, -2)
        True

    .. versionadded:: TODO
    """
    return search in array[fromindex:]


def is_empty(array):
    """Returns True if the :attr:`array` has a length of zero.

    Args:
        array (list): A list of values provided by the user.

    Returns:
        bool: True if the list is empty else False.

    Example:

        >>> is_empty([])
        True
        >>> is_empty([None])
        False

    .. versionadded:: TODO
    """
    return True if not array else False


def is_equal(array_one, array_two):
    """Returns True if :attr:`array_one` is equal to :attr:`array_two`.

    Args:
        array_one (list): First list of values provided by the user.
        array_two (list): Second list of values provided by the user.

    Returns:
        bool: True if both the arrays are equal else False.

    Example:

        >>> is_equal([1, 2], [1, 2])
        True
        >>> is_equal(['1'], [str(1)])
        True
        >>> is_equal([None], [])
        False
        >>> is_equal([1, 2], [2, 1])
        False
        >>> is_equal([], [])
        True

    .. versionadded:: TODO
    """
    return array_one == array_two


def last(array, num=1):
    """Returns the last element(s) in the array. When :attr:`num` is passed,
    returns the last :attr:`num` elements in the array.

    Args:
        array (list): List of values passed in by the user.
        num (int): Number passed in by the user.

    Returns:
        list: Returns an array of last :attr:`num` elements.

    Example:

        >>> last([11, 22, 33, 44], 1)
        [44]
        >>> last([11, 22, 33, 44], 3)
        [22, 33, 44]
        >>> last([11, 22, 33, 44], None)
        []
        >>> last([11, 22, 33, 44], -3)
        []
        >>> last([11, 22, 33, 44], 9)
        []

    .. versionadded:: TODO
    """
    num = 0 if (not num or num < 0) else num

    if len(array) < num:
        num = 0

    return array[(len(array) - num):]


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

#
# Helper methods not a part of the main API
#


def array_append(array, item, index=None):
    if not item:
        return array

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
