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
from omero.model import PointI


class Point201501Encoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'

    def encode(self, obj):
        v = super(Point201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', self.get_x(obj))
        self.set_if_not_none(v, 'Y', self.get_y(obj))
        return v

    def get_x(self, obj):
        return obj.cx

    def get_y(self, obj):
        return obj.cy


class Point201606Encoder(Point201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Point'

    def get_x(self, obj):
        return obj.x

    def get_y(self, obj):
        return obj.y


if SCHEMA_VERSION == '2015-01':
    encoder = (PointI, Point201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PointI, Point201606Encoder)
PointEncoder = encoder[1]
