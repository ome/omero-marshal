#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from omero_marshal import get_encoder


class TestBaseEncoder(object):

    def test_base_encoder(self, roi):
        encoder = get_encoder(roi.__class__)
        v = encoder.encode(roi)
        assert v == {
            '@id': 1L,
            '@type': 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI',
            'Name': 'the_name',
        }
