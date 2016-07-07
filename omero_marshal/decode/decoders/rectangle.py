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


# Handle differences in class naming between OMERO 5.1.x and 5.2.x
try:
    # OMERO 5.1.x
    from omero.model import RectI as RectangleI
except ImportError:
    # OMERO 5.2.x
    from omero.model import RectangleI


class Rectangle201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Rectangle'

    OMERO_CLASS = RectangleI

    def decode(self, data):
        v = super(Rectangle201501Decoder, self).decode(data)
        self.set_property(v, 'x', data.get('X'))
        self.set_property(v, 'y', data.get('Y'))
        self.set_property(v, 'width', data.get('Width'))
        self.set_property(v, 'height', data.get('Height'))
        return v


class Rectangle201606Decoder(Rectangle201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Rectangle'


if SCHEMA_VERSION == '2015-01':
    decoder = (Rectangle201501Decoder.TYPE, Rectangle201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Rectangle201606Decoder.TYPE, Rectangle201606Decoder)
RectangleDecoder = decoder[1]
