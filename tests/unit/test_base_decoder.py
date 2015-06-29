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

import json

from omero.model import RoiI
from omero_marshal import get_encoder, get_decoder


class TestBaseDecoder(object):

    def assert_roi(self, roi):
        assert roi.__class__ == RoiI
        assert roi.id.val == 1L
        assert roi.description.val == 'the_name'

    def test_base_decoder(self, roi):
        encoder = get_encoder(roi.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(roi)
        v = decoder.decode(v)
        self.assert_roi(v)

    def test_base_decoder_from_string(self):
        data_as_string = """{
    "@type": "http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI",
    "@id": 1,
    "Name": "the_name"
}"""
        data = json.loads(data_as_string)
        decoder = get_decoder(data['@type'])
        v = decoder.decode(data)
        self.assert_roi(v)
