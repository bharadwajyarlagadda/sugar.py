********
sugar.py
********

|version| |travis| |coveralls| |license|

Python utility library. Based on sugar Javascript Library.

Links
=====

- Project: https://github.com/bharadwajyarlagadda/sugar.py
- Documentation: http://sugarpy.readthedocs.io
- Pypi: https://pypi.python.org/pypi/sugar.py
- TravisCI: https://travis-ci.org/bharadwajyarlagadda/sugar.py

Features
========

- Supported on Python 2.7 and Python 3.3+.

Quickstart
==========

Install using pip:

::

    pip install sugar.py


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

    >>> _.filter([1, 2, 2, 4], value=2)
    [2, 2]
    >>> _.filter([1, 2, 2, 4], callback=lambda x: x > 1)
    [2, 2, 4]

    >>> _.subtract([1, 2, 3], 2)
    [1, 3]
    >>> _.subtract ([1, 2, 3], [1, 3])
    [2]
    >>> _.subtract([1, 2, 3], 4)
    [1, 2, 3]


.. |version| image:: https://img.shields.io/pypi/v/sugar.py.svg?style=flat-square
    :target: https://pypi.python.org/pypi/sugar.py/

.. |travis| image:: https://img.shields.io/travis/bharadwajyarlagadda/sugar.py/master.svg?style=flat-square
    :target: https://travis-ci.org/bharadwajyarlagadda/sugar.py

.. |coveralls| image:: https://img.shields.io/coveralls/bharadwajyarlagadda/sugar.py/master.svg?style=flat-square
    :target: https://coveralls.io/r/bharadwajyarlagadda/sugar.py

.. |license| image:: https://img.shields.io/pypi/l/sugar.py.svg?style=flat-square
    :target: https://pypi.python.org/pypi/sugar.py/
