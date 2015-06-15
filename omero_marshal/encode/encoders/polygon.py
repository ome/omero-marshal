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
from omero.model import PolygonI


class PolygonEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polygon'

    def encode(self, obj):
        v = super(PolygonEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Points', obj.points)
        return v

encoder = (PolygonI, PolygonEncoder)
