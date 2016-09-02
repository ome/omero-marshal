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
    X_PROPERTY_NAME = 'cx'
    Y_PROPERTY_NAME = 'cy'

    def encode(self, obj):
        v = super(Point201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', getattr(obj, self.X_PROPERTY_NAME))
        self.set_if_not_none(v, 'Y', getattr(obj, self.Y_PROPERTY_NAME))
        return v


class Point201606Encoder(Point201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Point'
    X_PROPERTY_NAME = 'x'
    Y_PROPERTY_NAME = 'y'


if SCHEMA_VERSION == '2015-01':
    encoder = (PointI, Point201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PointI, Point201606Encoder)
PointEncoder = encoder[1]
