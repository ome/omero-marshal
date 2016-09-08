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

from omero_marshal import get_encoder, get_decoder, SCHEMA_VERSION
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


@pytest.mark.skipif(SCHEMA_VERSION != "2015-01", reason="legacy classes")
class TestTransform201501Decoder():

    @pytest.mark.parametrize("transform_s,transform_o", TRANSFORMATIONS)
    def test_transforms(self, point, transform_s, transform_o):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        point.transform = transform_s
        v = encoder.encode(point)
        v = decoder.decode(v)
        assert v.transform.val == transform_o

    def test_none(self, point):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        point.transform = 'none'
        v = encoder.encode(point)
        v = decoder.decode(v)
        assert v.transform is None
