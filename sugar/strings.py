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
