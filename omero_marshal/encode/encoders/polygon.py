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
from omero.model import PolygonI


class Polygon201501Encoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polygon'

    def encode(self, obj):
        v = super(Polygon201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Points', obj.points)
        return v


class Polygon201606Encoder(Polygon201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Polygon'


if SCHEMA_VERSION == '2015-01':
    encoder = (PolygonI, Polygon201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PolygonI, Polygon201606Encoder)
PolygonEncoder = encoder[1]
