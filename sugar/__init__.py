# -*- coding: utf-8 -*-
"""sugar.py module.
"""

from .__pkg__ import (
    __description__,
    __url__,
    __version__,
    __author__,
    __email__,
    __license__
)

from .arrays import (
    average,
    clone,
    compact,
    construct,
    count,
    create,
    every,
    exclude,
    filter,
    subtract
)

from .predicates import (
    is_array,
    is_boolean,
    is_number,
    is_string
)
