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

    id = -1L
    A00 = None
    A10 = None
    A01 = None
    A11 = None
    A02 = None
    A12 = None
    DETAILS = None

    def __init__(self, *args):
        pass

    def convert_transform(self, transform):
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

        self.A00 = a[0]
        self.A10 = a[1]
        self.A01 = a[2]
        self.A11 = a[3]
        self.A02 = a[4]
        self.A12 = a[5]

    def __str__(self):
        return 'matrix(%s)' % ' '.join(map(str, [
            unwrap(self.A00),
            unwrap(self.A10),
            unwrap(self.A01),
            unwrap(self.A11),
            unwrap(self.A02),
            unwrap(self.A12),
            ]))

    def getA00(self):
        return self.A00

    def getA10(self):
        return self.A10

    def getA01(self):
        return self.A01

    def getA11(self):
        return self.A11

    def getA02(self):
        return self.A02

    def getA12(self):
        return self.A12

    def setA00(self, value):
        self.A00 = value

    def setA10(self, value):
        self.A10 = value

    def setA01(self, value):
        self.A01 = value

    def setA11(self, value):
        self.A11 = value

    def setA02(self, value):
        self.A02 = value

    def setA12(self, value):
        self.A12 = value
