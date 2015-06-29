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
from omero.model import PolygonI


class PolygonDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polygon'

    OMERO_CLASS = PolygonI

    def decode(self, data):
        v = super(PolygonDecoder, self).decode(data)
        v.points = self.to_rtype(data.get('Points'))
        return v

decoder = (PolygonDecoder.TYPE, PolygonDecoder)
