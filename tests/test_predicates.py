# -*- coding: utf-8 -*-

from .fixtures import parametrize

import sugar as _


@parametrize('case,expected', [
    (None, True),
    ([], False)
])
def test_is_none(case, expected):
    assert _.is_none(case) == expected
