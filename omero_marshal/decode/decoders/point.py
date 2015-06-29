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
from omero.model import PointI


class PointDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'

    OMERO_CLASS = PointI

    def decode(self, data):
        v = super(PointDecoder, self).decode(data)
        v.cx = self.to_rtype(data.get('X'))
        v.cy = self.to_rtype(data.get('Y'))
        return v

decoder = (PointDecoder.TYPE, PointDecoder)
