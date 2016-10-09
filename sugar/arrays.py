# -*- coding: utf-8 -*-

from __future__ import absolute_import


def construct(var, func):
    """Constructs an array of :attr:`var` length from the values of
    :attr:`func`.

    Args:
        var (int): Length of the array intended.
        func: A method that can take in each variable from the given range and
            return back a new value based on the method definition.

    Returns:
        list: A list of :attr:`func` values.

    Example:

        >>> def double(variable):
        ...     return variable * 2
        >>> construct(4, double)
        [0, 2, 4, 6]

    .. versionadded:: 0.1.0-dev
    """
    return [func(i) for i in range(0, var)]
