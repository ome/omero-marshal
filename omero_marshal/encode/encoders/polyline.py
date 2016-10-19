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
from omero.model import PolylineI


class Polyline201501Encoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polyline'

    def encode(self, obj):
        v = super(Polyline201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Points', obj.points)
        return v


class Polyline201606Encoder(Polyline201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Polyline'

    def encode(self, obj):
        v = super(Polyline201606Encoder, self).encode(obj)
        self.set_if_not_none(v, 'MarkerStart', obj.markerStart)
        self.set_if_not_none(v, 'MarkerEnd', obj.markerEnd)
        return v


if SCHEMA_VERSION == '2015-01':
    encoder = (PolylineI, Polyline201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PolylineI, Polyline201606Encoder)
PolylineEncoder = encoder[1]
