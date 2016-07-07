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
        self.set_property(v, 'fillColor', data.get('FillColor'))
        self.set_property(v, 'fillRule', data.get('FillRule'))
        self.set_property(v, 'fontFamily', data.get('FontFamily'))
        v.fontSize = self.to_unit(data.get('FontSize'))
        self.set_property(v, 'fontStyle', data.get('FontStyle'))
        self.set_property(v, 'strokeLineCap', data.get('LineCap'))
        self.set_property(v, 'locked', data.get('Locked'))
        self.set_property(v, 'strokeColor', data.get('StrokeColor'))
        self.set_property(v, 'strokeDashArray', data.get('StrokeDashArray'))
        v.strokeWidth = self.to_unit(data.get('StrokeWidth'))
        self.set_property(v, 'textValue', data.get('Text'))
        self.set_property(v, 'theC', data.get('TheC'))
        self.set_property(v, 'theT', data.get('TheT'))
        self.set_property(v, 'theZ', data.get('TheZ'))
        self.set_property(v, 'visibility', data.get('Visible'))
        self.set_property(
            v, 'transform', self.decode_transform(data.get('Transform')))
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
