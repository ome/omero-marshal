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

from .shape import ShapeEncoder
from omero.model import EllipseI
from omero_marshal import get_schema_version


class EllipseEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'


class Ellipse201606Encoder(EllipseEncoder):

    def encode(self, obj):
        v = super(Ellipse201606Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.x)
        self.set_if_not_none(v, 'Y', obj.y)
        self.set_if_not_none(v, 'RadiusX', obj.radiusX)
        self.set_if_not_none(v, 'RadiusY', obj.radiusY)
        return v


class Ellipse201501Encoder(EllipseEncoder):

    def encode(self, obj):
        v = super(Ellipse201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.cx)
        self.set_if_not_none(v, 'Y', obj.cy)
        self.set_if_not_none(v, 'RadiusX', obj.rx)
        self.set_if_not_none(v, 'RadiusY', obj.ry)
        return v

if get_schema_version() == '2015-01':
    encoder = (EllipseI, Ellipse201501Encoder)
elif get_schema_version() == '2016-06':
    encoder = (EllipseI, Ellipse201606Encoder)
