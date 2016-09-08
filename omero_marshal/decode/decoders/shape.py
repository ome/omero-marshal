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
        self.set_property(v, 'fillColor', data.get('FillColor'))
        self.set_property(v, 'fillRule', data.get('FillRule'))
        self.set_property(v, 'fontFamily', data.get('FontFamily'))
        v.fontSize = self.to_unit(data.get('FontSize'))
        self.set_property(v, 'fontStyle', data.get('FontStyle'))
        self.set_linecap(v, data)
        self.set_property(v, 'locked', data.get('Locked'))
        self.set_property(v, 'strokeColor', data.get('StrokeColor'))
        self.set_property(v, 'strokeDashArray', data.get('StrokeDashArray'))
        v.strokeWidth = self.to_unit(data.get('StrokeWidth'))
        self.set_property(v, 'textValue', data.get('Text'))
        self.set_property(v, 'theC', data.get('TheC'))
        self.set_property(v, 'theT', data.get('TheT'))
        self.set_property(v, 'theZ', data.get('TheZ'))
        self.set_visibility(v, data)
        transform = data.get('Transform')
        if transform:
            transform_decoder = self.ctx.get_decoder(transform['@type'])
            self.set_transform(v, transform_decoder.decode(transform))
        return v

    def set_visibility(self, v, data):
        self.set_property(v, 'visibility', data.get('Visible'))

    def set_linecap(self, v, data):
        self.set_property(v, 'strokeLineCap', data.get('LineCap'))

    def set_transform(self, v, transform):
        # For OMERO 5.1.x and OMERO 5.2.x, the transform is stored as a string
        # using the matrix(<a> <b> <c> <d> <e> <f>) style
        self.set_property(v, 'transform', str(transform))


class Shape201606Decoder(Shape201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Shape'

    def set_visibility(self, v, data):
        pass

    def set_linecap(self, v, data):
        pass

    def set_transform(self, v, transform):
        v.setTransform(transform)


if SCHEMA_VERSION == '2015-01':
    decoder = (Shape201501Decoder.TYPE, Shape201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Shape201606Decoder.TYPE, Shape201606Decoder)
ShapeDecoder = decoder[1]
