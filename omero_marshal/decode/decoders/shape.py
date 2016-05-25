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

from .annotation import AnnotatableDecoder
from omero.model import Shape


class ShapeDecoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Shape'

    OMERO_CLASS = Shape

    def decode(self, data):
        v = super(ShapeDecoder, self).decode(data)
        v.fillColor = self.to_rtype(data.get('FillColor'))
        v.fillRule = self.to_rtype(data.get('FillRule'))
        v.fontFamily = self.to_rtype(data.get('FontFamily'))
        v.fontSize = self.to_unit(data.get('FontSize'))
        v.fontStyle = self.to_rtype(data.get('FontStyle'))
        v.strokeLineCap = self.to_rtype(data.get('LineCap'))
        v.locked = self.to_rtype(data.get('Locked'))
        v.strokeColor = self.to_rtype(data.get('StrokeColor'))
        v.strokeDashArray = self.to_rtype(data.get('StrokeDashArray'))
        v.strokeWidth = self.to_unit(data.get('StrokeWidth'))
        v.textValue = self.to_rtype(data.get('Text'))
        v.theC = self.to_rtype(data.get('TheC'))
        v.theT = self.to_rtype(data.get('TheT'))
        v.theZ = self.to_rtype(data.get('TheZ'))
        v.visibility = self.to_rtype(data.get('Visible'))
        v.transform = self.to_rtype(
            self.decode_transform(data.get('Transform')))
        return v

    @staticmethod
    def decode_transform(transform):
        if not transform:
            return 'none'
        return 'matrix(%s)' % ' '.join(map(str, [
            transform['A00'],
            transform['A10'],
            transform['A01'],
            transform['A11'],
            transform['A02'],
            transform['A12'],
        ]))


decoder = (ShapeDecoder.TYPE, ShapeDecoder)
