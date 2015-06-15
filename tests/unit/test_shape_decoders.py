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

from omero_marshal import get_encoder, get_decoder


class TestShapeDecoder(object):

    def assert_roi(self, roi):
        assert roi.id.val == 1L
        assert roi.description.val == 'the_name'

    def assert_shape(self, shape):
        assert shape.fillColor.val == 0xffffffff
        assert shape.fillRule.val == 'solid'
        assert shape.strokeColor.val == 0xffff0000
        assert shape.strokeDashArray.val == 'inherit'
        assert shape.strokeWidth.val == 4
        assert shape.strokeLineCap.val == 'round'
        assert shape.textValue.val == 'the_text'
        assert shape.fontFamily.val == 'cursive'
        assert shape.fontSize.val == 12
        assert shape.fontStyle.val == 'italic'
        assert shape.visibility.val is True
        assert shape.locked.val is False
        assert shape.theZ.val == 3
        assert shape.theT.val == 2
        assert shape.theC.val == 1

    def assert_ellipse(self, ellipse):
        self.assert_shape(ellipse)
        assert ellipse.id.val == 1L
        assert ellipse.cx.val == 1.0
        assert ellipse.cy.val == 2.0
        assert ellipse.rx.val == 3.0
        assert ellipse.ry.val == 4.0

    def assert_rectangle(self, rectangle):
        self.assert_shape(rectangle)
        assert rectangle.id.val == 2L
        assert rectangle.x.val == 1.0
        assert rectangle.y.val == 2.0
        assert rectangle.width.val == 3.0
        assert rectangle.height.val == 4.0


class TestEllipseDecoder(TestShapeDecoder):

    def test_decoder(self, ellipse):
        encoder = get_encoder(ellipse.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(ellipse)
        v = decoder.decode(v)
        self.assert_ellipse(v)


class TestRectangeDecoder(TestShapeDecoder):

    def test_decoder(self, rectangle):
        encoder = get_encoder(rectangle.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(rectangle)
        v = decoder.decode(v)
        self.assert_rectangle(rectangle)


class TestPointDecoder(TestShapeDecoder):

    def test_decoder(self, point):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(point)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 3L
        assert v.cx.val == 1.0
        assert v.cy.val == 2.0


class TestPolylineDecoder(TestShapeDecoder):

    def test_decoder(self, polyline):
        encoder = get_encoder(polyline.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(polyline)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 4L
        assert v.points.val == '0,0 1,2 3,5'


class TestPolygonDecoder(TestShapeDecoder):

    def test_decoder(self, polygon):
        encoder = get_encoder(polygon.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(polygon)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 5L
        assert v.points.val == '0,0 1,2 3,5'


class TestRoiDecoder(TestShapeDecoder):

    def test_roi_with_shapes(self, roi_with_shapes):
        encoder = get_encoder(roi_with_shapes.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(roi_with_shapes)
        v = decoder.decode(v)
        self.assert_roi(v)
        assert v.sizeOfShapes() == 2
        ellipse, rectangle = v.copyShapes()
        self.assert_ellipse(ellipse)
        self.assert_rectangle(rectangle)
