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
from omero.model import LineI
from omero.rtypes import RDoubleI


class LineDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Line'

    OMERO_CLASS = LineI

    def decode(self, data):
        v = super(LineDecoder, self).decode(data)
        v.x1 = RDoubleI(data.get('X1'))
        v.y1 = RDoubleI(data.get('Y1'))
        v.x2 = RDoubleI(data.get('X2'))
        v.y2 = RDoubleI(data.get('Y2'))
        return v

decoder = (LineDecoder.TYPE, LineDecoder)
