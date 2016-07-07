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


class Ellipse201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'

    OMERO_CLASS = EllipseI
    X_PROPERTY_NAME = 'cx'
    Y_PROPERTY_NAME = 'cy'
    RADIUSX_PROPERTY_NAME = 'rx'
    RADIUSY_PROPERTY_NAME = 'ry'

    def decode(self, data):
        v = super(Ellipse201501Decoder, self).decode(data)
        self.set_property(v, self.X_PROPERTY_NAME, data.get('X'))
        self.set_property(v, self.Y_PROPERTY_NAME, data.get('Y'))
        self.set_property(v, self.RADIUSX_PROPERTY_NAME, data.get('RadiusX'))
        self.set_property(v, self.RADIUSY_PROPERTY_NAME, data.get('RadiusY'))
        return v


class Ellipse201606Decoder(Ellipse201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Ellipse'
    X_PROPERTY_NAME = 'x'
    Y_PROPERTY_NAME = 'y'
    RADIUSX_PROPERTY_NAME = 'radiusX'
    RADIUSY_PROPERTY_NAME = 'radiusY'


if SCHEMA_VERSION == '2015-01':
    decoder = (Ellipse201501Decoder.TYPE, Ellipse201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Ellipse201606Decoder.TYPE, Ellipse201606Decoder)
EllipseDecoder = decoder[1]
