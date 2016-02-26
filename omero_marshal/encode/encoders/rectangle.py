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

# Handle differences in class naming between OMERO 5.1.x and 5.2.x
try:
    # OMERO 5.1.x
    from omero.model import RectI as RectangleI
except ImportError:
    # OMERO 5.2.x
    from omero.model import RectangleI


class RectangleEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Rectangle'

    def encode(self, obj):
        v = super(RectangleEncoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.x)
        self.set_if_not_none(v, 'Y', obj.y)
        self.set_if_not_none(v, 'Width', obj.width)
        self.set_if_not_none(v, 'Height', obj.height)
        return v

encoder = (RectangleI, RectangleEncoder)
