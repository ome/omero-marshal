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
from .shape import ShapeDecoder
from omero.model import LineI


class Line201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Line'

    OMERO_CLASS = LineI

    def decode(self, data):
        v = super(Line201501Decoder, self).decode(data)
        self.set_property(v, 'x1', data.get('X1'))
        self.set_property(v, 'y1', data.get('Y1'))
        self.set_property(v, 'x2', data.get('X2'))
        self.set_property(v, 'y2', data.get('Y2'))
        return v


class Line201606Decoder(Line201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Line'

    def decode(self, data):
        v = super(Line201606Decoder, self).decode(data)
        self.set_property(v, 'markerStart', data.get('MarkerStart'))
        self.set_property(v, 'markerEnd', data.get('MarkerEnd'))
        return v


if SCHEMA_VERSION == '2015-01':
    decoder = (Line201501Decoder.TYPE, Line201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Line201606Decoder.TYPE, Line201606Decoder)
LineDecoder = decoder[1]
