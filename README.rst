|logo|

*Conway's Game of Life Terminal Eye Candy implemented in Python.*

|website| |release| |rtd| |license| |travis-ci| |codecov|

PConway
=======

**features**

* Play Conway's Game of Life on your terminal.

**Documentation**: https://pconway.readthedocs.io

**Repository**: https://github.com/terrencetec/pconway

.. contents::
   :depth: 2

Getting Started
===============

Dependencies
------------

Required
^^^^^^^^
* Package 1
* Package 2
* Package 3

Optional
^^^^^^^^
* Package 4

Note on installing dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In principle, if you are using :code:`pip`, you don't have to install
dependencies beforehand. When you install this package, :code`pip` will
automatically install the required libraries. However if you are using Conda
it is best to use its own package manager and not pip unless absolutely
necessary.

If you use conda:

.. code:: bash

   conda install -c conda-forge package1 package2

Now, let's say package 3 is not available, then we can use pip. But,
be sure to use :code:`which pip` to check if we are using the pip installed
on the conda environment and not the global one.

.. code:: bash

   pip install package3

Install from source
-------------------

.. code:: bash

   git clone https://github.com/terrencetec/pconway.git
   cd pconway
   pip install .

How to Contribute
=================

Try out the package and file an issue if you find any!


For Developers
==============

Standards and Tools
-------------------
Please comply with the following standards/guides as much as possible.

Coding style
^^^^^^^^^^^^
- **PEP 8**: https://www.python.org/dev/peps/pep-0008/

CHANGELOG
^^^^^^^^^
- **Keep a Changelog**: https://keepachangelog.com/en/1.0.0/

Versioning
^^^^^^^^^^
- **Semantic Versioning**: https://semver.org/spec/v2.0.0.html

Packaging
^^^^^^^^^
- **PyPA**: https://www.pypa.io
- **python-packaging**: https://python-packaging.readthedocs.io

Documentation
^^^^^^^^^^^^^
- **NumPy docstrings**: https://numpydoc.readthedocs.io/en/latest/format.html
- **Sphinx**: https://www.sphinx-doc.org/
- **Read The Docs**: https://readthedocs.org/
- **Documenting Python Code: A Complete Guide**: https://realpython.com/documenting-python-code/

Cheat sheet
-----------

Sphinx
^^^^^^

Generate documentation base, in docs/,

.. code:: bash

   sphinx-quickstart

Select separate build and source files when prompted.

Preview documentation page with modified source, in docs/

.. code:: bash

   make html

Open index.html with a browser (if this was set as the first page).

.. |logo| image:: docs/source/_static/logo.svg
    :alt: Logo
    :target: https://github.com/terrencetec/pconway

.. |website| image:: https://img.shields.io/badge/website-pconway-blue.svg
    :alt: Website
    :target: https://github.com/terrencetec/pconway

.. |release| image:: https://img.shields.io/github/v/release/terrencetec/pconway?include_prereleases
   :alt: Release
   :target: https://github.com/terrencetec/pconway/releases

.. |rtd| image:: https://readthedocs.org/projects/pconway/badge/?version=latest
   :alt: Read the Docs
   :target: https://pconway.readthedocs.io/

.. |license| image:: https://img.shields.io/github/license/terrencetec/pconway
    :alt: License
    :target: https://github.com/terrencetec/pconway/blob/master/LICENSE

.. |travis-ci| image:: https://travis-ci.com/terrencetec/pconway.svg?branch=master
    :alt: travis-ci
    :target: https://travis-ci.com/terrencetec/pconway

.. |codecov| image:: https://codecov.io/gh/terrencetec/pconway/branch/master/graph/badge.svg?token=NMEBAYFE2N
    :alt: codecov
    :target: https://codecov.io/gh/terrencetec/pconway
