# -*- coding: utf-8 -*-

from __future__ import absolute_import


def at(string, index=0, loop=False):
    """Return the character(s) at a given index. When :attr:`loop` is true,
    overshooting the end of the string will begin counting from the other end.
    :attr:`index` may be negative. If :attr:`index` is an array, multiple
    elements will be returned.

    Args:
        string (str): String value passed in by the user.
        index (int): Index value passed in by the user.
        loop (bool): If True, this method overshoots end of string and will
            begin counting from the other end.

    Returns:
        str/list: A character/List of characters based on the given index
            positions.

    Example:

        >>> at('example')
        'e'
        >>> at('example', 4)
        'p'
        >>> at('example', 8, True)
        'x'
        >>> at('example', [4, 8], True)
        ['p', 'x']
        >>> at('example', -4)
        'm'
        >>> at('example', [4, -4])
        ['p', 'm']
        >>> at('example', [4, -10], True)
        ['p', 'p']

    .. versionadded:: TODO
    """
    string = list(string)

    def get_index(value):
        if loop:
            if value > 0:
                while value > len(string):
                    value -= len(string)
            elif value < 0:
                while value < -len(string):
                    value += len(string)

        return value

    if isinstance(index, (list, tuple)):
        return [string[get_index(i)] for i in index]

    return string[get_index(index)]


def camelize(string, upper=True):
    """Converts underscores and hyphens to camel case. If :attr:`upper` is
    False, the :attr:`string` will be upperCamelCase.

    Args:
        string (str): String passed in by the user.
        upper (bool): If True, it will return UpperCamelCase else
            upperCamelCase.

    Returns:
        str: String converted to CamelCase.

    Example:

        >>> camelize('example')
        'Example'
        >>> camelize('example-test')
        'ExampleTest'
        >>> camelize('example_test-one')
        'ExampleTestOne'
        >>> camelize('example_test-one', False)
        'exampleTestOne'

    .. versionadded:: TODO
    """
    string = string.replace('_', '-')
    string = ''.join([i.title() for i in string.split('-')])

    if not upper:
        string = string[:1].lower() + string[1:]

    return string


def chars(string, callback=None):
    """Runs :func:`callable` against each character in the string and returns
    an array.

    Args:
        string (str): String passed in by the user.
        callback (func): Method to be run against each character in the string.

    Returns:
        list: List of chars after the :func:`callback` method is applied to
            all the chars in the given :attr:`string`.

    Example:

        >>> chars('example')
        ['e', 'x', 'a', 'm', 'p', 'l', 'e']
        >>> chars('example', lambda x: 'i' if x == 'e' else x)
        ['i', 'x', 'a', 'm', 'p', 'l', 'i']

    .. versionadded:: TODO
    """
    string = list(string)

    if callback:
        return [callback(char) for char in string]

    return string
