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

from ... import SCHEMA_VERSION
from .annotation import AnnotatableDecoder
from omero.model import ImageI


class Image201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Image'

    OMERO_CLASS = ImageI

    def decode(self, data):
        v = super(Image201501Decoder, self).decode(data)
        self.set_property(v, 'acquisitionDate', data.get('AcquisitionDate'))
        self.set_property(v, 'archived', data.get('omero:archived'))
        self.set_property(v, 'description', data.get('Description'))
        self.set_property(v, 'name', data.get('Name'))
        self.set_property(v, 'partial', data.get('omero:partial'))
        self.set_property(v, 'series', data.get('omero:series'))
        _format = data.get('omero:format')
        if _format is not None:
            format_decoder = self.ctx.get_decoder(_format['@type'])
            v.format = format_decoder.decode(_format)
        pixels = data.get('Pixels')
        if pixels is not None:
            pixels_decoder = self.ctx.get_decoder(pixels['@type'])
            v.addPixels(pixels_decoder.decode(pixels))
        return v


class Image201606Decoder(Image201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Image'


if SCHEMA_VERSION == '2015-01':
    decoder = (Image201501Decoder.TYPE, Image201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Image201606Decoder.TYPE, Image201606Decoder)
ImageDecoder = decoder[1]
