# -*- coding: utf-8 -*-

from .fixtures import parametrize

import sugar as _


@parametrize('args', [
    (0, 5),
    (2, 5),
    (-6, 0),
    (5.5, 11.7),
    (5.5, 6.5)
])
def test_random(args):
    assert args[0] <= _.random_(*args) <= args[1]
