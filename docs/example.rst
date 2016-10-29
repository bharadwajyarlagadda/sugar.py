.. _example:

Examples
========

Arrays
------

.. code-block:: python

    >>> import sugar as _

    >>> _.add([11, 22, 33], 88)
    [11, 22, 33, 88]
    >>> _.add([11, 22, 33], 88, 1)
    [11, 88, 22, 33]
    >>> _.add([11, 22, 33], [44, 55])
    [11, 22, 33, 44, 55]
    >>> _.add([11, 22, 33], [44, 55, 66, 77], 1)
    [11, 44, 55, 66, 77, 22, 33]

    >>> _.append([11, 22, 33], 88)
    [11, 22, 33, 88]
    >>> _.append([11, 22, 33], 88, 1)
    [11, 88, 22, 33]
    >>> _.append([11, 22, 33], [44, 55])
    [11, 22, 33, 44, 55]
    >>> _.append([11, 22, 33], [44, 55, 66, 77], 1)
    [11, 44, 55, 66, 77, 22, 33]

    >>> float(_.average([1, 2, 3]))
    2.0

    >>> _.clone([1, 2, 3])
    [1, 2, 3]

    >>> _.compact([1, None, 2, False, 3])
    [1, 2, False, 3]
    >>> _.compact([1, None, '', False, 2], all=True)
    [1, 2]

    >>> _.construct(4, lambda x: x * 2)
    [0, 2, 4, 6]

    >>> _.count([1, 2, 3, 3], 3)
    2

    >>> _.create('abc def 109;cd')
    ['a', 'b', 'c', ' ', 'd', 'e', 'f', ' ', '1', '0', '9', ';', 'c', 'd']
    >>> _.create(1234)
    [1234]
    >>> _.create([11, 22, 33, 44], copy=True)
    [11, 22, 33, 44]
    >>> _.create(True)
    [True]
    >>> _.create()
    []

    >>> _.every([2, 2, 2], 2)
    True
    >>> _.every([2, 2, 3], 2)
    False

    >>> _.exclude([11, 22, 33], 22)
    [11, 33]
    >>> _.exclude([11, 22, 33], 44)
    [11, 22, 33]
    >>> _.exclude([11, 22, 33], [11, 22])
    [33]

    >>> _.filter_([1, 2, 2, 4], value=2)
    [2, 2]
    >>> _.filter_([1, 2, 2, 4], callback=lambda x: x > 1)
    [2, 2, 4]

    >>> _.first([11, 22, 33, 44], 1)
    [11]
    >>> _.first([11, 22, 33, 44], None)
    []
    >>> _.first([11, 22, 33, 44], -3)
    []
    >>> _.first([11, 22, 33, 44], 9)
    [11, 22, 33, 44]

    >>> _.from_([11, 22, 33], 1)
    [22, 33]
    >>> _.from_([11, 22, 33])
    [11, 22, 33]
    >>> _.from_([11, 22, 33], 2)
    [33]
    >>> _.from_([11, 22, 33], None)
    [11, 22, 33]

    >>> _.includes([11, 22, 33], 22, 0)
    True
    >>> _.includes([11, 22, 33], 22, 1)
    True
    >>> _.includes([11, 22, 33], 22, 2)
    False
    >>> _.includes([11, 22, 33], 11, None)
    True
    >>> _.includes([11, 22, 33], 33)
    True
    >>> _.includes([11, 22, 33], 22, -1)
    False
    >>> _.includes([11, 22, 33], 22, -2)
    True

    >>> _.is_empty([])
    True
    >>> _.is_empty([None])
    False

    >>> _.is_equal([1, 2], [1, 2])
    True
    >>> _.is_equal(['1'], [str(1)])
    True
    >>> _.is_equal([None], [])
    False
    >>> _.is_equal([1, 2], [2, 1])
    False
    >>> _.is_equal([], [])
    True

    >>> _.last([11, 22, 33, 44], 1)
    [44]
    >>> _.last([11, 22, 33, 44], 3)
    [22, 33, 44]
    >>> _.last([11, 22, 33, 44], None)
    []
    >>> _.last([11, 22, 33, 44], -3)
    []
    >>> _.last([11, 22, 33, 44], 9)
    []

    >>> _.subtract([1, 2, 3], 2)
    [1, 3]
    >>> _.subtract ([1, 2, 3], [1, 3])
    [2]
    >>> _.subtract([1, 2, 3], 4)
    [1, 2, 3]

Numbers
-------

.. code-block:: python

    >>> import sugar as _

    >>> _.is_even(6)
    True
    >>> _.is_even(7)
    False

    >>> _.is_multiple_of(6, 2)
    True
    >>> _.is_multiple_of(5, 2)
    False
    >>> _.is_multiple_of(1.5, 3)
    False
    >>> _.is_multiple_of(1.5, 0.5)
    True

    >>> _.is_odd(6)
    False
    >>> _.is_odd(7)
    True

    >>> _.is_prime(5)
    True
    >>> _.is_prime(7)
    True
    >>> _.is_prime(4)
    False
    >>> _.is_prime(727021)
    True

    >>> result = _.random_(5, 6)
    >>> assert 5 <= result <= 6
    >>> result = _.random_(5)
    >>> assert 0 <= result <= 5


Predicates
----------

.. code-block:: python

    >>> import sugar as _

    >>> _.is_none(None)
    True
    >>> _.is_none([])
    False

