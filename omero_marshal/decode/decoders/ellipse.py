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
from omero.model import EllipseI
from omero.rtypes import RDoubleI


class Ellipse201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'

    OMERO_CLASS = EllipseI

    def decode(self, data):
        v = super(Ellipse201501Decoder, self).decode(data)
        self.set_x(v, RDoubleI(data.get('X')))
        self.set_y(v, RDoubleI(data.get('Y')))
        self.set_radiusX(v, RDoubleI(data.get('RadiusX')))
        self.set_radiusY(v, RDoubleI(data.get('RadiusY')))
        return v

    @staticmethod
    def set_x(obj, value):
        obj.cx = value

    @staticmethod
    def set_y(obj, value):
        obj.cy = value

    @staticmethod
    def set_radiusX(obj, value):
        obj.rx = value

    @staticmethod
    def set_radiusY(obj, value):
        obj.ry = value


class Ellipse201606Decoder(Ellipse201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Ellipse'

    @staticmethod
    def set_x(obj, value):
        obj.x = value

    @staticmethod
    def set_y(obj, value):
        obj.y = value

    @staticmethod
    def set_radiusX(obj, value):
        obj.radiusX = value

    @staticmethod
    def set_radiusY(obj, value):
        obj.radiusY = value


if SCHEMA_VERSION == '2015-01':
    decoder = (Ellipse201501Decoder.TYPE, Ellipse201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Ellipse201606Decoder.TYPE, Ellipse201606Decoder)
EllipseDecoder = decoder[1]
