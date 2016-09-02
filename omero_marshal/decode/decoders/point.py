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


class Point201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'

    OMERO_CLASS = PointI
    X_PROPERTY_NAME = 'cx'
    Y_PROPERTY_NAME = 'cy'

    def decode(self, data):
        v = super(Point201501Decoder, self).decode(data)
        self.set_property(v, self.X_PROPERTY_NAME, data.get('X'))
        self.set_property(v, self.Y_PROPERTY_NAME, data.get('Y'))
        return v


class Point201606Decoder(Point201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Point'
    X_PROPERTY_NAME = 'x'
    Y_PROPERTY_NAME = 'y'


if SCHEMA_VERSION == '2015-01':
    decoder = (Point201501Decoder.TYPE, Point201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Point201606Decoder.TYPE, Point201606Decoder)
PointDecoder = decoder[1]
