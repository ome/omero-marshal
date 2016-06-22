.. image:: https://travis-ci.org/openmicroscopy/omero-marshal.png
   :target: http://travis-ci.org/openmicroscopy/omero-marshal

.. image:: https://badge.fury.io/py/omero-marshal.svg
    :target: https://badge.fury.io/py/omero-marshal

OMERO Marshal
=============

Extensible marshaling code to transform various OMERO objects into
dictionaries which can then be marshalled using JSON or alternative
encodings.

Requirements
============

* OMERO.py 5.1.x, 5.2.x
* Python 2.6+

Development Installation
========================

1. Clone the repository::

        git clone git@github.com:openmicroscopy/omero-marshal.git

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

* http://www.openmicroscopy.org/Schemas/Documentation/Generated/OME-2015-01/ome.html
* http://www.openmicroscopy.org/site/support/omero5.1/developers/Model/Units.html
* https://www.openmicroscopy.org/site/support/omero5.1/developers/Model/KeyValuePairs.html
