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

from .. import Decoder
from omero.model import Shape
from omero.rtypes import rtype


class ShapeDecoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Shape'

    OMERO_CLASS = Shape

    def decode(self, data):
        v = super(ShapeDecoder, self).decode(data)
        v.fillColor = rtype(data.get('FillColor'))
        v.fillRule = rtype(data.get('FillRule'))
        v.fontFamily = rtype(data.get('FontFamily'))
        v.fontSize = rtype(data.get('FontSize'))
        v.fontStyle = rtype(data.get('FontStyle'))
        v.strokeLineCap = rtype(data.get('LineCap'))
        v.locked = rtype(data.get('Locked'))
        v.strokeColor = rtype(data.get('StrokeColor'))
        v.strokeDashArray = rtype(data.get('StrokeDashArray'))
        v.strokeWidth = rtype(data.get('StrokeWidth'))
        v.textValue = rtype(data.get('Text'))
        v.theC = rtype(data.get('TheC'))
        v.theT = rtype(data.get('TheT'))
        v.theZ = rtype(data.get('TheZ'))
        v.visibility = rtype(data.get('Visible'))
        return v

decoder = (ShapeDecoder.TYPE, ShapeDecoder)
