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
from omero.model import LineI


class Line201501Encoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Line'

    def encode(self, obj):
        v = super(Line201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X1', obj.x1)
        self.set_if_not_none(v, 'Y1', obj.y1)
        self.set_if_not_none(v, 'X2', obj.x2)
        self.set_if_not_none(v, 'Y2', obj.y2)
        return v


class Line201606Encoder(Line201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Line'

    def encode(self, obj):
        v = super(Line201606Encoder, self).encode(obj)
        self.set_if_not_none(v, 'MarkerStart', obj.markerStart)
        self.set_if_not_none(v, 'MarkerEnd', obj.markerEnd)
        return v


if SCHEMA_VERSION == '2015-01':
    encoder = (LineI, Line201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (LineI, Line201606Encoder)
LineEncoder = encoder[1]
