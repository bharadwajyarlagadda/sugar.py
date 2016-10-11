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

    >>> import sugar

    >>> float(sugar.average([1, 2, 3]))
    2.0

    >>> sugar.construct(4, lambda x: x * 2)
    [0, 2, 4, 6]

    >>> sugar.count([1, 2, 3, 3], 3)
    2

    >>> sugar.subtract([1, 2, 3], 2)
    [1, 3]
    >>> sugar.subtract ([1, 2, 3], [1, 3])
    [2]
    >>> sugar.subtract([1, 2, 3], 4)
    [1, 2, 3]


.. |version| image:: https://img.shields.io/pypi/v/sugar.py.svg?style=flat-square
    :target: https://pypi.python.org/pypi/sugar.py/

.. |travis| image:: https://img.shields.io/travis/bharadwajyarlagadda/sugar.py/master.svg?style=flat-square
    :target: https://travis-ci.org/bharadwajyarlagadda/sugar.py

.. |coveralls| image:: https://img.shields.io/coveralls/bharadwajyarlagadda/sugar.py/master.svg?style=flat-square
    :target: https://coveralls.io/r/bharadwajyarlagadda/sugar.py

.. |license| image:: https://img.shields.io/pypi/l/sugar.py.svg?style=flat-square
    :target: https://pypi.python.org/pypi/sugar.py/
