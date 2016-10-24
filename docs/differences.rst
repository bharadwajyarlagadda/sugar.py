.. _differences:

SugarJS Differences
===================


Naming Conventions
------------------

sugar.py adheres to the following conventions:

- Function names use ``snake_case`` instead of ``camelCase``.
- Any SugarJS function that shares its name with a reserved Python keyword will have an ``_`` appended after it (e.g. ``from`` in sugarjs would be ``from_`` in sugar.py).
