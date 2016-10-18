# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""Python 2/3 compatibility

    Some py2/py3 compatibility support based on a stripped down
    version of six so we don't have to depend on a specific version
    of it.

    Borrowed from
    https://github.com/mitsuhiko/flask/blob/master/flask/_compat.py
"""

import sys
from decimal import Decimal

PY3 = sys.version_info[0] == 3
PY26 = sys.version_info[0:2] == (2, 6)

if PY3:
    string_types = (str,)
    number_types = (int, float, Decimal)
else:
    string_types = (str, unicode)
    number_types = (int, long, float, Decimal)
