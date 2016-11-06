# -*- coding: utf-8 -*-

from .fixtures import parametrize

import sugar as _


@parametrize('case,index,loop,expected', [
    ('test example', 4, False, " "),
    ('test example', [4, 7], False, [' ', 'a']),
    ('example', 8, True, 'x'),
    ('example', [8, 10], True, ['x', 'm']),
    ('example', -2, False, 'l'),
    ('example', [-8, -10], True, ['e', 'p']),
    ('example', [4, 8], True, ['p', 'x']),
    ('example', (4, -4), False, ['p', 'm'])
])
def test_at(case, index, loop, expected):
    assert _.at(case, index, loop) == expected


@parametrize('case,upper,expected', [
    ('example', True, 'Example'),
    ('example-test', True, 'ExampleTest'),
    ('example_test-one', True, 'ExampleTestOne'),
    ('example_test-one', False, 'exampleTestOne')
])
def test_camelize(case, upper, expected):
    assert _.camelize(case, upper) == expected
