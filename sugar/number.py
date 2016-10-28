# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import random
import math


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
