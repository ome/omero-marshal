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

from omero_marshal import get_decoder, ROI_SCHEMA_URL


class TestRegisterDecoder(object):

    def test_roi_decoder_registered(self):
        decoder = get_decoder('%s#ROI' % ROI_SCHEMA_URL)
        assert decoder is not None
