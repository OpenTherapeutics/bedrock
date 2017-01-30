bedrock
=======

Yet another collection of seemingly essential Python features and utilities for
building non-trivial applications.

`Documentation <Package Documentation>`_

Supports Python 2.7+, 3.5+.

Installation
------------

::

    $ pip install bedrock


Development
-----------

*Note:* Development instructions assume you have `pip <https://pip.pypa.io/en/stable/>`_ and 
`virtualenv <https://virtualenv.pypa.io/en/stable/>`_ installed.

::

    $ git clone https://github.com/OpenTherapeutics/bedrock.git
    $ virtualenv venv
    $ source venv/bin/activate

For convenience, `invoke <http://www.pyinvoke.org/>`_ is used, via the ``tasks.py``
file to facilitate development::

    $ pip install invoke
    $ inv install
    $ inv develop

Testing
-------

After running ``inv develop`` (see above), several additional packages are installed
for testing purposes. ``bedrock`` uses `pytest <http://doc.pytest.org/en/latest/>`_
for testing, along with `tox <https://tox.readthedocs.io/en/latest/>`_ and
`coverage <https://coverage.readthedocs.io/en/coverage-4.3.4/>`_

Simple test run::

    $ inv test

Run tests across supported Python versions::

    $ tox
