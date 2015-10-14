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
from omero.model.enums import UnitsLength
from omero.rtypes import RDoubleI
from omero.model import LengthI


class TestShapeDecoder(object):

    def assert_annotations(self, o):
        assert o.annotationLinksLoaded
        boolean_annotation, comment_annotation, double_annotation, \
            long_annotation, tag_annotation, term_annotation, \
            timestamp_annotation, xml_annotation = \
            [v.child for v in o.copyAnnotationLinks()]
        assert boolean_annotation.ns.val == 'boolean_annotation'
        assert boolean_annotation.description.val == 'the_description'
        assert boolean_annotation.boolValue.val
        assert comment_annotation.ns.val == 'comment_annotation'
        assert comment_annotation.description.val == 'the_description'
        assert comment_annotation.textValue.val == 'text_value'
        assert double_annotation.ns.val == 'double_annotation'
        assert double_annotation.description.val == 'the_description'
        assert double_annotation.doubleValue.val == 1.0
        assert long_annotation.ns.val == 'long_annotation'
        assert long_annotation.description.val == 'the_description'
        assert long_annotation.longValue.val == 1L
        assert tag_annotation.ns.val == 'tag_annotation'
        assert tag_annotation.description.val == 'the_description'
        assert tag_annotation.textValue.val == 'tag_value'
        assert term_annotation.ns.val == 'term_annotation'
        assert term_annotation.description.val == 'the_description'
        assert term_annotation.termValue.val == 'term_value'
        assert timestamp_annotation.ns.val == 'timestamp_annotation'
        assert timestamp_annotation.description.val == 'the_description'
        assert timestamp_annotation.timeValue.val == 1L

    def assert_roi(self, roi, has_annotations=False):
        assert roi.id.val == 1L
        assert roi.description.val == 'the_description'
        assert roi.name.val == 'the_name'
        if not has_annotations:
            assert not roi.annotationLinksLoaded
        else:
            self.assert_annotations(roi)

    def assert_shape(self, shape):
        assert shape.fillColor.val == 0xffffffff
        assert shape.fillRule.val == 'solid'
        assert shape.strokeColor.val == 0xffff0000
        assert shape.strokeDashArray.val == 'inherit'
        assert shape.strokeWidth.__class__ is LengthI
        assert shape.strokeWidth.getUnit() == UnitsLength.PIXEL
        assert shape.strokeWidth.getValue() == 4
        assert shape.strokeLineCap.val == 'round'
        assert shape.textValue.val == 'the_text'
        assert shape.fontFamily.val == 'cursive'
        assert shape.fontSize.__class__ is LengthI
        assert shape.fontSize.getUnit() == UnitsLength.POINT
        assert shape.fontSize.getValue() == 12
        assert shape.fontStyle.val == 'italic'
        assert shape.visibility.val is True
        assert shape.locked.val is False
        assert shape.theZ.val == 3
        assert shape.theT.val == 2
        assert shape.theC.val == 1

    def assert_ellipse(self, ellipse):
        self.assert_shape(ellipse)
        assert ellipse.id.val == 1L
        assert ellipse.cx.__class__ is RDoubleI
        assert ellipse.cx.val == 1.0
        assert ellipse.cy.__class__ is RDoubleI
        assert ellipse.cy.val == 2.0
        assert ellipse.rx.__class__ is RDoubleI
        assert ellipse.rx.val == 3.0
        assert ellipse.ry.__class__ is RDoubleI
        assert ellipse.ry.val == 4.0

    def assert_rectangle(self, rectangle):
        self.assert_shape(rectangle)
        assert rectangle.id.val == 2L
        assert rectangle.x.__class__ is RDoubleI
        assert rectangle.x.val == 1.0
        assert rectangle.y.__class__ is RDoubleI
        assert rectangle.y.val == 2.0
        assert rectangle.width.__class__ is RDoubleI
        assert rectangle.width.val == 3.0
        assert rectangle.height.__class__ is RDoubleI
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
        assert v.cx.__class__ is RDoubleI
        assert v.cx.val == 1.0
        assert v.cy.__class__ is RDoubleI
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

    def assert_roi_with_shapes(self, v, has_annotations=False):
        self.assert_roi(v, has_annotations=has_annotations)
        assert v.sizeOfShapes() == 2
        ellipse, rectangle = v.copyShapes()
        self.assert_ellipse(ellipse)
        self.assert_rectangle(rectangle)

    def test_roi_with_shapes(self, roi_with_shapes):
        encoder = get_encoder(roi_with_shapes.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(roi_with_shapes)
        v = decoder.decode(v)
        self.assert_roi_with_shapes(v)

    def test_roi_with_shapes_and_annotations(
            self, roi_with_shapes_and_annotations):
        encoder = get_encoder(roi_with_shapes_and_annotations.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(roi_with_shapes_and_annotations)
        v = decoder.decode(v)
        self.assert_roi_with_shapes(v, has_annotations=True)
