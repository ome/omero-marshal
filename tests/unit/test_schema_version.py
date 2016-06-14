#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from omero_marshal import get_schema_version
import pytest


class SchemaFixture(object):
    """
    Fixture to test matching of omero version and schema version
    """

    def __init__(self, omero_version, schema_version):
        self.omero_version = omero_version
        self.schema_version = schema_version

SFS = (SchemaFixture("5.1.0-ice35-b40", "2015-01"),
       SchemaFixture("5.2.0-ice35-b12", "2015-01"),
       SchemaFixture("5.2.4-ice35-b23", "2015-01"),
       SchemaFixture("5.3.0-m2-ice35-b20", "2016-06"))


@pytest.mark.parametrize("f", SFS, ids=[x.omero_version for x in SFS])
def test_schema_version(f):
    assert get_schema_version(f.omero_version) == f.schema_version
