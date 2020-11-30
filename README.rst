.. image:: https://github.com/ome/omero-marshal/workflows/Tox/badge.svg
    :target: https://github.com/ome/omero-marshal/actions

.. image:: https://img.shields.io/pypi/v/omero-marshal.svg
   :alt: PyPI
   :target: https://pypi.org/project/omero-marshal/

OMERO Marshal
=============

Extensible marshaling code to transform various OMERO objects into
dictionaries which can then be marshalled using JSON or alternative
encodings.

Requirements
============

* OMERO.py 5.6 or newer
* Python 3.6 or newer

Development Installation
========================

1. Clone the repository::

        git clone git@github.com:ome/omero-marshal.git

2. Set up a virtualenv (http://www.pip-installer.org/) and activate it::

        curl -O -k https://raw.github.com/pypa/virtualenv/master/virtualenv.py
        python virtualenv.py omero-marshal
        source omero-marshal/bin/activate
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

Running Tests
=============

Using py.test to run the unit tests::

    	py.test tests/unit/

License
=======

This project, similar to many Open Microscopy Environment (OME) projects, is
licensed under the terms of the GNU General Public License (GPL) v2 or later.

Reference
=========

* https://www.openmicroscopy.org/Schemas/Documentation/Generated/OME-2015-01/ome.html
* https://docs.openmicroscopy.org/latest/omero/developers/Model/Units.html
* https://docs.openmicroscopy.org/latest/omero/developers/Model/KeyValuePairs.html
