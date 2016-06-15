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

from .annotation import AnnotatableEncoder
from omero.model import Shape
from omero.rtypes import unwrap
from math import sin, cos, radians


class ShapeEncoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Shape'

    def encode(self, obj):
        v = super(ShapeEncoder, self).encode(obj)
        self.set_if_not_none(v, 'FillColor', obj.fillColor)
        self.set_if_not_none(v, 'FillRule', obj.fillRule)
        self.set_if_not_none(v, 'FontFamily', obj.fontFamily)
        self.set_if_not_none(v, 'FontSize', obj.fontSize)
        self.set_if_not_none(v, 'FontStyle', obj.fontStyle)
        self.set_if_not_none(v, 'LineCap', obj.strokeLineCap)
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
        self.set_if_not_none(v, 'Visible', obj.visibility)
        return v

    @staticmethod
    def encode_transform(transform):
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
            '@type': 'http://www.openmicroscopy.org/Schemas/ROI/2015-01'
                     '#AffineTransform',
            'A00': a[0],
            'A10': a[1],
            'A01': a[2],
            'A11': a[3],
            'A02': a[4],
            'A12': a[5],
        }


encoder = (Shape, ShapeEncoder)
