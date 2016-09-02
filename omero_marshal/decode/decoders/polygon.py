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
from omero.model import PolygonI


class Polygon201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polygon'

    OMERO_CLASS = PolygonI

    def decode(self, data):
        v = super(Polygon201501Decoder, self).decode(data)
        self.set_property(v, 'points', data.get('Points'))
        return v


class Polygon201606Decoder(Polygon201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Polygon'


if SCHEMA_VERSION == '2015-01':
    decoder = (Polygon201501Decoder.TYPE, Polygon201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Polygon201606Decoder.TYPE, Polygon201606Decoder)
PolygonDecoder = decoder[1]
