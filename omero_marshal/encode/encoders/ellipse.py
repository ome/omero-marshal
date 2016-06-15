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

    def encode(self, obj):
        v = super(Ellipse201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', self.get_x(obj))
        self.set_if_not_none(v, 'Y', self.get_y(obj))
        self.set_if_not_none(v, 'RadiusX', self.get_radiusX(obj))
        self.set_if_not_none(v, 'RadiusY', self.get_radiusY(obj))
        return v

    @staticmethod
    def get_x(obj):
        return obj.cx

    @staticmethod
    def get_y(obj):
        return obj.cy

    @staticmethod
    def get_radiusX(obj):
        return obj.rx

    @staticmethod
    def get_radiusY(obj):
        return obj.ry


class Ellipse201606Encoder(Ellipse201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Ellipse'

    @staticmethod
    def get_x(obj):
        return obj.x

    @staticmethod
    def get_y(obj):
        return obj.y

    @staticmethod
    def get_radiusX(obj):
        return obj.radiusX

    @staticmethod
    def get_radiusY(obj):
        return obj.radiusY


if SCHEMA_VERSION == '2015-01':
    encoder = (EllipseI, Ellipse201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (EllipseI, Ellipse201606Encoder)
EllipseEncoder = encoder[1]
