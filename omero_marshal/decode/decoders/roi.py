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
from omero.model import RoiI


class Roi201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'

    OMERO_CLASS = RoiI

    def decode(self, data):
        v = super(Roi201501Decoder, self).decode(data)
        self.set_property(v, 'name', data.get('Name'))
        self.set_property(v, 'description', data.get('Description'))
        for shape in data.get('shapes', list()):
            shape_decoder = self.ctx.get_decoder(shape['@type'])
            v.addShape(shape_decoder.decode(shape))
        return v


class Roi201606Decoder(Roi201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#ROI'


if SCHEMA_VERSION == '2015-01':
    decoder = (Roi201501Decoder.TYPE, Roi201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Roi201606Decoder.TYPE, Roi201606Decoder)
RoiDecoder = decoder[1]
