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
from omero.model import PointI
from omero.rtypes import RDoubleI


class Point201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'

    OMERO_CLASS = PointI

    def decode(self, data):
        v = super(Point201501Decoder, self).decode(data)
        self.set_x(v, RDoubleI(data.get('X')))
        self.set_y(v, RDoubleI(data.get('Y')))
        return v

    def set_x(self, obj, value):
        obj.cx = value

    def set_y(self, obj, value):
        obj.cy = value


class Point201606Decoder(Point201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Point'

    def set_x(self, obj, value):
        obj.x = value

    def set_y(self, obj, value):
        obj.y = value


if SCHEMA_VERSION == '2015-01':
    decoder = (Point201501Decoder.TYPE, Point201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Point201606Decoder.TYPE, Point201606Decoder)
PointDecoder = decoder[1]
