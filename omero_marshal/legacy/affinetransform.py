#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from math import sin, cos, radians
from omero.rtypes import unwrap


class AffineTransformI(object):
    """
    Class handling OMERO 5.1 and OMERO 5.2 transform string representations.
    Its fields and methods are directly mirroring the
    omero.model.AffineTransform class introduced in OMERO 5.3 to reduce the
    complexity of the transform encoders/decoders.
    """

    def __init__(self, *args):
        # Set the id to -1 to differentiate the marshalled transform from
        # objects
        # Setting the id also allows the transform decoder to inherit the
        # superclass decode() method
        self.id = -1L
        self._svg_transform = None
        self._a00 = None
        self._a10 = None
        self._a01 = None
        self._a11 = None
        self._a02 = None
        self._a12 = None

    def convert_svg_transform(self, transform):
        """
        Converts a string representing a SVG transform into
        AffineTransform fields.
        See https://www.w3.org/TR/SVG/coords.html#TransformAttribute for the
        specification of the transform strings. skewX and skewY are not
        supported.
        Raises:
            ValueError: If transform is not a valid and supported SVG
            transform.
        """

        tr, args = transform[:-1].split('(')
        a = map(float, args.split(' '))

        # Handle various string tranformations
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

        self._svg_transform = transform
        self._a00 = a[0]
        self._a10 = a[1]
        self._a01 = a[2]
        self._a11 = a[3]
        self._a02 = a[4]
        self._a12 = a[5]

    def __str__(self):
        """Returns a string matrix representation of the transform"""
        return 'matrix(%s)' % ' '.join(map(str, [
            unwrap(self._a00),
            unwrap(self._a10),
            unwrap(self._a01),
            unwrap(self._a11),
            unwrap(self._a02),
            unwrap(self._a12),
            ]))

    @property
    def svg_transform(self):
        """Retrieves the string containing the SVG transform"""
        return self._svg_transform

    def getA00(self):
        return self._a00

    def getA10(self):
        return self._a10

    def getA01(self):
        return self._a01

    def getA11(self):
        return self._a11

    def getA02(self):
        return self._a02

    def getA12(self):
        return self._a12

    def setA00(self, value):
        self._a00 = value

    def setA10(self, value):
        self._a10 = value

    def setA01(self, value):
        self._a01 = value

    def setA11(self, value):
        self._a11 = value

    def setA02(self, value):
        self._a02 = value

    def setA12(self, value):
        self._a12 = value
