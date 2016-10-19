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
from omero.model import PolylineI


class Polyline201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polyline'

    OMERO_CLASS = PolylineI

    def decode(self, data):
        v = super(Polyline201501Decoder, self).decode(data)
        self.set_property(v, 'points', data.get('Points'))
        return v


class Polyline201606Decoder(Polyline201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Polyline'

    def decode(self, data):
        v = super(Polyline201606Decoder, self).decode(data)
        self.set_property(v, 'markerStart', data.get('MarkerStart'))
        self.set_property(v, 'markerEnd', data.get('MarkerEnd'))
        return v


if SCHEMA_VERSION == '2015-01':
    decoder = (Polyline201501Decoder.TYPE, Polyline201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Polyline201606Decoder.TYPE, Polyline201606Decoder)
PolylineDecoder = decoder[1]
