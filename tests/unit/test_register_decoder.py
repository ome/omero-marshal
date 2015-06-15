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

from omero_marshal import get_decoder


class TestRegisterDecoder(object):

    def test_roi_decoder_registered(self):
        decoder = get_decoder(
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'
        )
        assert decoder is not None
