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
from math import sin, cos, radians


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
        self.set_if_not_none(
            v, 'Transform', self.encode_transform(obj.transform))
        self.set_linecap(v, obj)
        self.set_visible(v, obj)
        return v

    def set_linecap(self, v, obj):
        self.set_if_not_none(v, 'LineCap', obj.strokeLineCap)

    def set_visible(self, v, obj):
        self.set_if_not_none(v, 'Visible', obj.visibility)

    def get_transform_type(self):
        return 'http://www.openmicroscopy.org/Schemas/ROI/2015-01' \
            '#AffineTransform'

    def encode_transform(self, transform):
        transform = unwrap(transform)
        if not transform or transform == 'none':
            return

        tr, args = transform[:-1].split('(')
        a = map(float, args.split(' '))

        if tr == 'matrix':
            pass
        elif tr == 'translate':
            a = [1.0, 0.0, 0.0, 1.0, a[0], a[1] if len(a) > 1 else 0.0]
        elif tr == 'scale':
            a = [a[0], 0.0, 0.0, a[-1], 0.0, 0.0]
        elif tr == 'rotate':
            x = a[1] if len(a) > 1 else 0.0
            y = a[2] if len(a) > 1 else 0.0
            rad = radians(a[0])
            s = sin(rad)
            c = cos(rad)
            a = [
                c,
                s,
                -s,
                c,
                x * (1 - c) + y * s,
                -x * s + y * (1 - c),
            ]
        else:
            raise ValueError('Unknown transformation "%s"' % transform)

        return {
            '@type': self.get_transform_type(),
            'A00': a[0],
            'A10': a[1],
            'A01': a[2],
            'A11': a[3],
            'A02': a[4],
            'A12': a[5],
        }


class Shape201606Encoder(Shape201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Shape'

    def set_linecap(self, v, obj):
        pass

    def set_visible(self, v, obj):
        pass

    def get_transform_type(self):
        return 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
            '#AffineTransform'

    def encode_transform(self, transform):
        if not transform:
            return None
        if (transform.getA00() is None and transform.getA10() is None and
                transform.getA01() is None and transform.getA11() is None and
                transform.getA02() is None and transform.getA12() is None):
            return None

        return {
            '@type': self.get_transform_type(),
            'A00': transform.getA00().val,
            'A10': transform.getA10().val,
            'A01': transform.getA01().val,
            'A11': transform.getA11().val,
            'A02': transform.getA02().val,
            'A12': transform.getA12().val,
        }

if SCHEMA_VERSION == '2015-01':
    encoder = (Shape, Shape201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (Shape, Shape201606Encoder)
ShapeEncoder = encoder[1]
