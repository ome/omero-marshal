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
from omero.rtypes import RDoubleI

# Handle differences in class naming between OMERO 5.1.x and 5.2.x
try:
    # OMERO 5.1.x
    from omero.model import RectI as RectangleI
except ImportError:
    # OMERO 5.2.x
    from omero.model import RectangleI


class RectangleDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Rectangle'

    OMERO_CLASS = RectangleI

    def decode(self, data):
        v = super(RectangleDecoder, self).decode(data)
        v.x = RDoubleI(data.get('X'))
        v.y = RDoubleI(data.get('Y'))
        v.width = RDoubleI(data.get('Width'))
        v.height = RDoubleI(data.get('Height'))
        return v

decoder = (RectangleDecoder.TYPE, RectangleDecoder)
