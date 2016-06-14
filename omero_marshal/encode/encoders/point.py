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
from omero.model import PointI
from omero_marshal import SCHEMA_VERSION


class PointEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'


class Point201606Encoder(PointEncoder):

    def encode(self, obj):
        v = super(Point201606Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.x)
        self.set_if_not_none(v, 'Y', obj.y)
        return v


class Point201501Encoder(PointEncoder):

    def encode(self, obj):
        v = super(Point201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.cx)
        self.set_if_not_none(v, 'Y', obj.cy)
        return v

if SCHEMA_VERSION == '2015-01':
    encoder = (PointI, Point201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PointI, Point201606Encoder)
