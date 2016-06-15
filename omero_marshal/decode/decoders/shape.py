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
from .annotation import AnnotatableDecoder
from omero.model import Shape


class Shape201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Shape'

    OMERO_CLASS = Shape

    def decode(self, data):
        v = super(Shape201501Decoder, self).decode(data)
        v.fillColor = self.to_rtype(data.get('FillColor'))
        v.fillRule = self.to_rtype(data.get('FillRule'))
        v.fontFamily = self.to_rtype(data.get('FontFamily'))
        v.fontSize = self.to_unit(data.get('FontSize'))
        v.fontStyle = self.to_rtype(data.get('FontStyle'))
        v.locked = self.to_rtype(data.get('Locked'))
        v.strokeColor = self.to_rtype(data.get('StrokeColor'))
        v.strokeDashArray = self.to_rtype(data.get('StrokeDashArray'))
        v.strokeWidth = self.to_unit(data.get('StrokeWidth'))
        v.textValue = self.to_rtype(data.get('Text'))
        v.theC = self.to_rtype(data.get('TheC'))
        v.theT = self.to_rtype(data.get('TheT'))
        v.theZ = self.to_rtype(data.get('TheZ'))
        self.set_visibility(v, data)
        self.set_linecap(v, data)
        v.transform = self.to_rtype(
            self.decode_transform(data.get('Transform')))
        return v

    def set_visibility(self, obj, data):
        obj.visibility = self.to_rtype(data.get('Visible'))

    def set_linecap(self, obj, data):
        obj.strokeLineCap = self.to_rtype(data.get('LineCap'))

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


class Shape201606Decoder(Shape201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Shape'

    def set_visibility(self, obj, data):
        pass

    def set_linecap(self, obj, value):
        pass

if SCHEMA_VERSION == '2015-01':
    decoder = (Shape201501Decoder.TYPE, Shape201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Shape201606Decoder.TYPE, Shape201606Decoder)
ShapeDecoder = decoder[1]
