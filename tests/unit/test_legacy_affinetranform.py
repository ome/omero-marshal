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

from omero_marshal.legacy.affinetransform import AffineTransformI
import pytest


TRANSFORMATIONS = [
    (
        'matrix(1.0 0.0 0.0 1.0 0.0 0.0)',
        'matrix(1.0 0.0 0.0 1.0 0.0 0.0)',
    ),
    (
        'translate(3 4)',
        'matrix(1.0 0.0 0.0 1.0 3.0 4.0)',
    ),
    (
        'translate(5)',
        'matrix(1.0 0.0 0.0 1.0 5.0 0.0)',
    ),
    (
        'scale(1.5 2.5)',
        'matrix(1.5 0.0 0.0 2.5 0.0 0.0)',
    ),
    (
        'scale(1.5)',
        'matrix(1.5 0.0 0.0 1.5 0.0 0.0)',
    ),
    (
        'rotate(45)',
        'matrix(0.707106781187 0.707106781187 -0.707106781187 0.707106781187 '
        '0.0 0.0)',
    ),
    (
        'rotate(45 50 100)',
        'matrix(0.707106781187 0.707106781187 -0.707106781187 0.707106781187 '
        '85.3553390593 -6.06601717798)',
    ),
    (
        'rotate(60)',
        'matrix(0.5 0.866025403784 -0.866025403784 0.5 '
        '0.0 0.0)',
    ),
    (
        'rotate(60 50 100)',
        'matrix(0.5 0.866025403784 -0.866025403784 0.5 '
        '111.602540378 6.69872981078)'
    ),
]


INVALID_TRANSFORMS = (
    '', 'none', 'matrix()', 'scale()', 'translate(three)', 'skewX(1)')

class TestLegacyAffineTransform():

    @pytest.mark.parametrize("transform", INVALID_TRANSFORMS)
    def test_invalid_transform(self, transform):
        t = AffineTransformI()
        with pytest.raises(ValueError):
            t.convert_svg_transform(transform)

    @pytest.mark.parametrize("transform_s,transform_o", TRANSFORMATIONS)
    def test_convert_transform(self, transform_s, transform_o):
        t = AffineTransformI()
        t.convert_svg_transform(transform_s)
        assert str(t) == transform_o
