OMERO ROI to JSON project
=========================

Marshaling code to transform OMERO ROI objects into JSON.

Requirements
============

* OMERO.py 5.1.x
* Python 2.6+

Development Installation
========================

1. Clone the repository

        git clone git@github.com:glencoesoftware/roi-to-json.git

2. Set up a virtualenv (http://www.pip-installer.org/) and activate it

        curl -O -k https://raw.github.com/pypa/virtualenv/master/virtualenv.py
        python virtualenv.py roi-to-json
        source roi-to-json/bin/activate
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

Running Tests
=============

Using py.test to run the unit tests:

    	py.test tests/unit/

Reference
=========

