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
from .shape import ShapeEncoder
from omero.model import EllipseI


class Ellipse201501Encoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'
    X_PROPERTY_NAME = 'cx'
    Y_PROPERTY_NAME = 'cy'
    RADIUSX_PROPERTY_NAME = 'rx'
    RADIUSY_PROPERTY_NAME = 'ry'

    def encode(self, obj):
        v = super(Ellipse201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', getattr(obj, self.X_PROPERTY_NAME))
        self.set_if_not_none(v, 'Y', getattr(obj, self.Y_PROPERTY_NAME))
        self.set_if_not_none(
            v, 'RadiusX', getattr(obj, self.RADIUSX_PROPERTY_NAME))
        self.set_if_not_none(
            v, 'RadiusY', getattr(obj, self.RADIUSY_PROPERTY_NAME))
        return v


class Ellipse201606Encoder(Ellipse201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Ellipse'
    X_PROPERTY_NAME = 'x'
    Y_PROPERTY_NAME = 'y'
    RADIUSX_PROPERTY_NAME = 'radiusX'
    RADIUSY_PROPERTY_NAME = 'radiusY'


if SCHEMA_VERSION == '2015-01':
    encoder = (EllipseI, Ellipse201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (EllipseI, Ellipse201606Encoder)
EllipseEncoder = encoder[1]
