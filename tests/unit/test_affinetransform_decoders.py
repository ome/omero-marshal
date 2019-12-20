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

from omero_marshal import get_encoder, get_decoder, SCHEMA_VERSION
from omero.rtypes import RDoubleI


class TestIdentityTranform():

    def assert_identity_transform(self, v):
        assert v.getA00().__class__ is RDoubleI
        assert v.getA00().val == 1.0
        assert v.getA01().__class__ is RDoubleI
        assert v.getA01().val == 0.0
        assert v.getA10().__class__ is RDoubleI
        assert v.getA10().val == 0.0
        assert v.getA11().__class__ is RDoubleI
        assert v.getA11().val == 1.0
        assert v.getA02().__class__ is RDoubleI
        assert v.getA02().val == 0.0
        assert v.getA12().__class__ is RDoubleI
        assert v.getA12().val == 0.0

    def test_decoder(self,  identity_transform):
        encoder = get_encoder(identity_transform.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(identity_transform)
        v = decoder.decode(v)
        self.assert_identity_transform(v)

    def test_shape_decoder(self,  point, identity_transform):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        if SCHEMA_VERSION == '2015-01':
            point.transform = identity_transform.svg_transform
        else:
            point.transform = identity_transform
        v = encoder.encode(point)
        v = decoder.decode(v)
        t = v.transform
        if SCHEMA_VERSION == '2015-01':
            assert t.val == 'matrix(1.0 0.0 0.0 1.0 0.0 0.0)'
        else:
            assert t.id.val == 8
            self.assert_identity_transform(t)


class TestTranslationTranform():

    def assert_translation_transform(self, v):
        assert v.getA00().__class__ is RDoubleI
        assert v.getA00().val == 1.0
        assert v.getA01().__class__ is RDoubleI
        assert v.getA01().val == 0.0
        assert v.getA10().__class__ is RDoubleI
        assert v.getA10().val == 0.0
        assert v.getA11().__class__ is RDoubleI
        assert v.getA11().val == 1.0
        assert v.getA02().__class__ is RDoubleI
        assert v.getA02().val == 3.0
        assert v.getA12().__class__ is RDoubleI
        assert v.getA12().val == 4.0

    def test_decoder(self,  translation_transform):
        encoder = get_encoder(translation_transform.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(translation_transform)
        v = decoder.decode(v)
        self.assert_translation_transform(v)

    def test_shape_decoder(self,  point, translation_transform):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        if SCHEMA_VERSION == '2015-01':
            point.transform = translation_transform.svg_transform
        else:
            point.transform = translation_transform
        v = encoder.encode(point)
        v = decoder.decode(v)
        t = v.transform
        if SCHEMA_VERSION == '2015-01':
            assert t.val == 'matrix(1.0 0.0 0.0 1.0 3.0 4.0)'
        else:
            assert t.id.val == 8
            self.assert_translation_transform(t)


class TestRotationTranform():

    def assert_rotation_transform(self, v):
        assert v.getA00().__class__ is RDoubleI
        assert v.getA00().val == 0.7071067811865476
        assert v.getA10().__class__ is RDoubleI
        assert v.getA10().val == 0.7071067811865475
        assert v.getA01().__class__ is RDoubleI
        assert v.getA01().val == -0.7071067811865475
        assert v.getA11().__class__ is RDoubleI
        assert v.getA11().val == 0.7071067811865476
        assert v.getA02().__class__ is RDoubleI
        assert v.getA02().val == 85.35533905932736
        assert v.getA12().__class__ is RDoubleI
        assert v.getA12().val == -6.066017177982129

    def test_decoder(self,  rotation_transform):
        encoder = get_encoder(rotation_transform.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(rotation_transform)
        v = decoder.decode(v)
        self.assert_rotation_transform(v)

    def test_shape_decoder(self,  point, rotation_transform):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        if SCHEMA_VERSION == '2015-01':
            point.transform = rotation_transform.svg_transform
        else:
            point.transform = rotation_transform
        v = encoder.encode(point)
        v = decoder.decode(v)
        t = v.transform
        if SCHEMA_VERSION == '2015-01':
            assert t.val == (
                'matrix(0.707106781187 0.707106781187 -0.707106781187 '
                '0.707106781187 85.3553390593 -6.06601717798)')
        else:
            assert t.id.val == 8
            self.assert_rotation_transform(t)


class TestScaleTranform():

    def assert_scale_transform(self, v):
        assert v.getA00().__class__ is RDoubleI
        assert v.getA00().val == 1.5
        assert v.getA01().__class__ is RDoubleI
        assert v.getA01().val == 0.0
        assert v.getA10().__class__ is RDoubleI
        assert v.getA10().val == 0.0
        assert v.getA11().__class__ is RDoubleI
        assert v.getA11().val == 2.5
        assert v.getA02().__class__ is RDoubleI
        assert v.getA02().val == 0.0
        assert v.getA12().__class__ is RDoubleI
        assert v.getA12().val == 0.0

    def test_decoder(self,  scale_transform):
        encoder = get_encoder(scale_transform.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(scale_transform)
        v = decoder.decode(v)
        self.assert_scale_transform(v)

    def test_shape_decoder(self,  point, scale_transform):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        if SCHEMA_VERSION == '2015-01':
            point.transform = scale_transform.svg_transform
        else:
            point.transform = scale_transform
        v = encoder.encode(point)
        v = decoder.decode(v)
        t = v.transform
        if SCHEMA_VERSION == '2015-01':
            assert t.val == 'matrix(1.5 0.0 0.0 2.5 0.0 0.0)'
        else:
            assert t.id.val == 8
            self.assert_scale_transform(t)
