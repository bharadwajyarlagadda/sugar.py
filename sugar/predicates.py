# -*- coding: utf-8 -*-

from ._compat import string_types, number_types


def is_array(obj):
    """Validates whether the given value is a list or not.

    Args:
        obj (mixed): Value passed in by the user.

    Returns:
        bool: True if the given object is a list. False if the given object is
            not a list.

    Example:

        >>> is_array([1, 2, 3, 4])
        True
        >>> is_array('abcd')
        False
        >>> is_array(1234)
        False

    .. versionadded:: TODO
    """
    return not is_boolean(obj) and isinstance(obj, list)


def is_boolean(obj):
    """Validates whether the given object is a boolean or not.

    Args:
        obj (mixed): Value passed in by the user.

    Returns:
        bool: True if the given object is a boolean. False if the given object
            is not a boolean.

    Example:

        >>> is_boolean(True)
        True
        >>> is_boolean('abcd')
        False
        >>> is_boolean(1234)
        False

    .. versionadded:: TODO
    """
    return isinstance(obj, bool)


def is_none(value):
    """Returns True if the :attr:`value` is None.

    Args:
        value (mixed): Value passed in by the user.

    Returns:
        bool: True if the given value is None else False

    Example:

        >>> is_none(None)
        True
        >>> is_none([])
        False

    .. versionadded:: TODO
    """
    return value is None


def is_number(value):
    """Validates whether the given value is an integer/float.

    Args:
        value (mixed): Value passed in by the user.

    Returns:
        bool: True if the given object is a number. False if the given object
            is not a number.

    Example:

        >>> is_number(1234)
        True
        >>> is_number('abcd')
        False
        >>> is_number([11, 22, 33, 44])
        False

    .. versionadded:: TODO
    """
    return not is_boolean(value) and isinstance(value, number_types)


def is_string(value):
    """Validates whether the given value is a string or not.

    Args:
        value (mixed): Value passed in by the user.

    Returns:
        bool: True if the given object is a string. False if the given object
            is not a string.

    Example:

        >>> is_string('abcd')
        True
        >>> is_string(1234)
        False
        >>> is_string([11, 22, 33, 44])
        False

    .. versionadded:: TODO
    """
    return not is_boolean(value) and isinstance(value, string_types)
