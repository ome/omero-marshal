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
from omero.model import PointI
from omero.rtypes import RDoubleI
from omero_marshal import SCHEMA_VERSION


class PointDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'

    OMERO_CLASS = PointI


class Point201501Decoder(PointDecoder):

    def decode(self, data):
        v = super(PointDecoder, self).decode(data)
        v.cx = RDoubleI(data.get('X'))
        v.cy = RDoubleI(data.get('Y'))
        return v


class Point201606Decoder(PointDecoder):

    def decode(self, data):
        v = super(PointDecoder, self).decode(data)
        v.x = RDoubleI(data.get('X'))
        v.y = RDoubleI(data.get('Y'))
        return v


if SCHEMA_VERSION == '2015-01':
    decoder = (Point201501Decoder.TYPE, Point201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Point201606Decoder.TYPE, Point201606Decoder)
