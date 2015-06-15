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

from omero_marshal import get_encoder, get_decoder


class TestBaseDecoder(object):

    def test_base_decoder(self, roi):
        encoder = get_encoder(roi.__class__)()
        decoder = get_decoder(encoder.TYPE)()
        v = encoder.encode(roi)
        v = decoder.decode(v)
        assert v.__class__ == roi.__class__
        assert v.id.val == 1L
        assert v.description.val == 'the_name'
