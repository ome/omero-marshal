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
from .annotation import AnnotatableEncoder
from omero.model import Shape
from omero.rtypes import unwrap


class Shape201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Shape'

    def encode(self, obj):
        v = super(Shape201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'FillColor', obj.fillColor)
        self.set_if_not_none(v, 'FillRule', obj.fillRule)
        self.set_if_not_none(v, 'FontFamily', obj.fontFamily)
        self.set_if_not_none(v, 'FontSize', obj.fontSize)
        self.set_if_not_none(v, 'FontStyle', obj.fontStyle)
        self.set_if_not_none(v, 'Locked', obj.locked)
        self.set_if_not_none(v, 'StrokeColor', obj.strokeColor)
        self.set_if_not_none(v, 'StrokeDashArray', obj.strokeDashArray)
        self.set_if_not_none(v, 'StrokeWidth', obj.strokeWidth)
        self.set_if_not_none(v, 'Text', obj.textValue)
        self.set_if_not_none(v, 'TheC', obj.theC)
        self.set_if_not_none(v, 'TheT', obj.theT)
        self.set_if_not_none(v, 'TheZ', obj.theZ)
        transform = self.get_transform(obj.transform)
        if transform:
            transform_encoder = self.ctx.get_encoder(transform.__class__)
            self.set_if_not_none(
                v, 'Transform', transform_encoder.encode(transform))
        self.set_linecap(v, obj)
        self.set_visible(v, obj)
        return v

    def set_linecap(self, v, obj):
        self.set_if_not_none(v, 'LineCap', obj.strokeLineCap)

    def set_visible(self, v, obj):
        self.set_if_not_none(v, 'Visible', obj.visibility)

    def get_transform(self, transform):
        transform = unwrap(transform)
        if not transform:
            return

        # For OMERO 5.1.x and OMERO 5.2.x the unwrapped transform is a string.
        # To facilitate the encoding we construct an internal AffineTransform
        # object and use convert_svg_transform() to map the SVG string
        # representation into the fields defined by the schema.
        from omero_marshal.legacy.affinetransform import AffineTransformI
        t = AffineTransformI()
        try:
            t.convert_svg_transform(transform)
        except ValueError:
            # Means the string is an invalid or unsupported SVG transform
            return
        return t


class Shape201606Encoder(Shape201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Shape'

    def set_linecap(self, v, obj):
        pass

    def set_visible(self, v, obj):
        pass

    def get_transform(self, transform):
        if not transform:
            return None
        if (transform.getA00() is None and transform.getA10() is None and
                transform.getA01() is None and transform.getA11() is None and
                transform.getA02() is None and transform.getA12() is None):
            return None
        return transform


if SCHEMA_VERSION == '2015-01':
    encoder = (Shape, Shape201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (Shape, Shape201606Encoder)
ShapeEncoder = encoder[1]
