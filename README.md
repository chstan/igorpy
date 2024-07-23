====
Igor
====

:Authors: W. Trevor King <wking@tremily.us>;
          Paul Kienzle <paul.kienzle@nist.gov>
:License: GNU General Public License, version 3+

Python parsers for Igor Binary Waves (.ibw) and Packed Experiment
(.pxp) files written by WaveMetrics' IGOR Pro software.

Installation
============

Packages
--------

If `igor` already exists in your package manager's repository, you
should install `igor` in the usual way.

Gentoo
~~~~~~

I've packaged `igor` for Gentoo.  You need layman_ and my `wtk
overlay`_.  Install with::

    # emerge -av app-portage/layman
    # layman --add wtk
    # emerge -av sci-misc/igor

Dependencies
------------

If you're installing by hand or packaging `igor` for another
distribution, you'll need the following dependencies:

===========  =================  ============================
Package      Debian_            Gentoo_
===========  =================  ============================
Numpy_       python-numpy       dev-python/numpy
Matplotlib_  python-matplotlib  dev-python/matplotlib
Nose_        python-nose        dev-python/nose
===========  =================  ============================

Installing by hand
------------------

`igor` is available as a Git_ repository::

    $ git clone git://tremily.us/igor.git

See the homepage_ for details.  To install the checkout, run the
standard::

    $ python setup.py install

You can also automate this installation with pip_::

    $ pip install igor

Usage
=====

See the docstrings and unit tests for examples using the Python API.
The package also installs to scripts, ``igorbinarywave.py`` and
``igorpackedexperiment.py`` which can be used to dump files to stdout.
For details on their usage, use the ``--help`` option.  For example::

  $ igorbinarywave.py --help

For users transitioning from igor.py_, there's a compatibility module
exposing the old interface.  Just change::

  import igor

to::

  import igor.igorpy as igor

in your calling code.

Testing
=======

Run internal unit tests with::

    $ nosetests --with-doctest --doctest-tests igor test

The data in the ``test/data`` directory is in the Git repository, but
it is not bundled with the source code.  If you want the test data,
you'll have to clone the Git repository or download a snapshot.

Licence
=======

This project is distributed under the `GNU Lesser General Public
License Version 3`_ or greater, see the ``COPYING`` file distributed
with the project for details.

Maintenance
===========

Maintainer
----------

W. Trevor King
wking@tremily.us
Copyright 2008-2012

Release procedure
-----------------

When a new version of the package is ready, increment __version__
in ``igor/__init__.py`` and run update-copyright_::

    $ update-copyright.py

to update the copyright blurbs.  Then run::

    $ python setup.py sdist upload

This will place a new version on PyPI.


.. _layman: http://layman.sourceforge.net/
.. _wtk overlay: http://blog.tremily.us/posts/Gentoo_overlay/
.. _Debian: http://www.debian.org/
.. _Gentoo: http://www.gentoo.org/
.. _NumPy: http://numpy.scipy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Git: http://git-scm.com/
.. _homepage: http://blog.tremily.us/posts/igor/
.. _pip: http://pypi.python.org/pypi/pip
.. _igor.py: http://pypi.python.org/pypi/igor.py
.. _GNU Lesser General Public License Version 3:
    http://www.gnu.org/licenses/lgpl.txt
.. _update-copyright: http://blog.tremily.us/posts/update-copyright/
