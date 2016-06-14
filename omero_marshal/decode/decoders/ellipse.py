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

from .shape import ShapeDecoder
from omero.model import EllipseI
from omero.rtypes import RDoubleI
from omero_marshal import SCHEMA_VERSION


class EllipseDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'

    OMERO_CLASS = EllipseI


class Ellipse201501Decoder(EllipseDecoder):

    def decode(self, data):
        v = super(Ellipse201501Decoder, self).decode(data)
        v.cx = RDoubleI(data.get('X'))
        v.cy = RDoubleI(data.get('Y'))
        v.rx = RDoubleI(data.get('RadiusX'))
        v.ry = RDoubleI(data.get('RadiusY'))
        return v


class Ellipse201606Decoder(EllipseDecoder):

    def decode(self, data):
        v = super(Ellipse201606Decoder, self).decode(data)
        v.x = RDoubleI(data.get('X'))
        v.y = RDoubleI(data.get('Y'))
        v.radiusX = RDoubleI(data.get('RadiusX'))
        v.radiusY = RDoubleI(data.get('RadiusY'))
        return v


if SCHEMA_VERSION == '2015-01':
    decoder = (Ellipse201501Decoder.TYPE, Ellipse201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Ellipse201606Decoder.TYPE, Ellipse201606Decoder)
