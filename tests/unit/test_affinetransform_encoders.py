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

from omero_marshal import get_encoder, SCHEMA_VERSION, ROI_SCHEMA_URL
from omero.rtypes import rdouble

try:
    # Import transform classes introduced in OMERO 5.3.0
    from omero.model import AffineTransformI
except ImportError:
    # Use internal AffineTransformI classes for OMERO 5.1.x and OMERO 5.2.x
    from omero_marshal.legacy.affinetransform import AffineTransformI

import pytest


def create_affine_transform(a00, a10, a01, a11, a02, a12):
    t = AffineTransformI()
    t.setA00(rdouble(a00))
    t.setA10(rdouble(a10))
    t.setA01(rdouble(a01))
    t.setA11(rdouble(a11))
    t.setA02(rdouble(a02))
    t.setA12(rdouble(a12))
    return t


TRANSFORMATION_TYPE = '%s#AffineTransform' % ROI_SCHEMA_URL

TRANSFORMATIONS = [
    (
        'matrix(1.0 0.0 0.0 1.0 0.0 0.0)',
        create_affine_transform(1.0, 0.0, 0.0, 1.0, 0.0, 0.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 1.0,
            'A10': 0.0,
            'A01': 0.0,
            'A11': 1.0,
            'A02': 0.0,
            'A12': 0.0,
        }
    ),
    (
        'none',
        None,
        None
    ),
    (
        'translate(3 4)',
        create_affine_transform(1.0, 0.0, 0.0, 1.0, 3.0, 4.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 1.0,
            'A10': 0.0,
            'A01': 0.0,
            'A11': 1.0,
            'A02': 3.0,
            'A12': 4.0,
        }
    ),
    (
        'translate(5)',
        create_affine_transform(1.0, 0.0, 0.0, 1.0, 5.0, 0.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 1.0,
            'A10': 0.0,
            'A01': 0.0,
            'A11': 1.0,
            'A02': 5.0,
            'A12': 0.0,
        }
    ),
    (
        'scale(1.5 2.5)',
        create_affine_transform(1.5, 0.0, 0.0, 2.5, 0.0, 0.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 1.5,
            'A10': 0.0,
            'A01': 0.0,
            'A11': 2.5,
            'A02': 0.0,
            'A12': 0.0,
        }
    ),
    (
        'scale(1.5)',
        create_affine_transform(1.5, 0.0, 0.0, 1.5, 0.0, 0.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 1.5,
            'A10': 0.0,
            'A01': 0.0,
            'A11': 1.5,
            'A02': 0.0,
            'A12': 0.0,
        }
    ),
    (
        'rotate(45)',
        create_affine_transform(
            0.7071067811865476, 0.7071067811865475, -0.7071067811865475,
            0.7071067811865476, 0.0, 0.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 0.7071067811865476,
            'A10': 0.7071067811865475,
            'A01': -0.7071067811865475,
            'A11': 0.7071067811865476,
            'A02': 0.0,
            'A12': 0.0,
        }
    ),
    (
        'rotate(45 50 100)',
        create_affine_transform(
            0.7071067811865476, 0.7071067811865475, -0.7071067811865475,
            0.7071067811865476, 85.35533905932736, -6.066017177982129),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 0.7071067811865476,
            'A10': 0.7071067811865475,
            'A01': -0.7071067811865475,
            'A11': 0.7071067811865476,
            'A02': 85.35533905932736,
            'A12': -6.066017177982129,
        }
    ),
    (
        'rotate(60)',
        create_affine_transform(
            0.5000000000000001, 0.8660254037844386, -0.8660254037844386,
            0.5000000000000001, 0.0, 0.0),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 0.5000000000000001,
            'A10': 0.8660254037844386,
            'A01': -0.8660254037844386,
            'A11': 0.5000000000000001,
            'A02': 0.0,
            'A12': 0.0,
        }
    ),
    (
        'rotate(60 50 100)',
        create_affine_transform(
            0.5000000000000001, 0.8660254037844386, -0.8660254037844386,
            0.5000000000000001, 111.60254037844385, 6.698729810778055),
        {
            '@type': TRANSFORMATION_TYPE,
            'A00': 0.5000000000000001,
            'A10': 0.8660254037844386,
            'A01': -0.8660254037844386,
            'A11': 0.5000000000000001,
            'A02': 111.60254037844385,
            'A12': 6.698729810778055,
        }
    ),

]


if SCHEMA_VERSION == '2015-01':
    AFFINE_TRANSFORMS = [(x[0], x[2]) for x in TRANSFORMATIONS]
else:
    AFFINE_TRANSFORMS = [(x[1], x[2]) for x in TRANSFORMATIONS]


class TestAffineTransformEncoder():

    @pytest.mark.parametrize("transform_s,transform_o", AFFINE_TRANSFORMS)
    def test_shape_transforms(self, point, transform_s, transform_o):
        point.transform = transform_s
        encoder = get_encoder(point.__class__)
        v = encoder.encode(point)
        if not transform_o:
            assert 'Transform' not in v
        else:
            if SCHEMA_VERSION == '2015-01':
                transform_o['@id'] = -1
            else:
                transform_o['omero:details'] = {'@type': 'TBD#Details'}
            assert v['Transform'] == transform_o
