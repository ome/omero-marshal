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

from omero_marshal import get_encoder


class TestShapeEncoder(object):

    def assert_roi(self, roi):
        assert roi['@id'] == 1L
        assert roi['Name'] == 'the_name'
        assert roi['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'
        assert roi['omero:details'] == {'@type': 'TBD#Details'}

    def assert_shape(self, shape):
        assert shape['FillColor'] == 0xffffffff
        assert shape['FillRule'] == 'solid'
        assert shape['StrokeColor'] == 0xffff0000
        assert shape['StrokeDashArray'] == 'inherit'
        assert shape['StrokeWidth'] == 4
        assert shape['LineCap'] == 'round'
        assert shape['Text'] == 'the_text'
        assert shape['FontFamily'] == 'cursive'
        assert shape['FontSize'] == 12
        assert shape['FontStyle'] == 'italic'
        assert shape['Visible'] is True
        assert shape['Locked'] is False
        assert shape['TheZ'] == 3
        assert shape['TheT'] == 2
        assert shape['TheC'] == 1
        assert shape['omero:details'] == {'@type': 'TBD#Details'}

    def assert_ellipse(self, ellipse):
        self.assert_shape(ellipse)
        assert ellipse['@id'] == 1L
        assert ellipse['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'
        assert ellipse['X'] == 1.0
        assert ellipse['Y'] == 2.0
        assert ellipse['RadiusX'] == 3.0
        assert ellipse['RadiusY'] == 4.0

    def assert_rectangle(self, rectangle):
        self.assert_shape(rectangle)
        assert rectangle['@id'] == 2L
        assert rectangle['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Rectangle'
        assert rectangle['X'] == 1.0
        assert rectangle['Y'] == 2.0
        assert rectangle['Width'] == 3.0
        assert rectangle['Height'] == 4.0


class TestEllipseEncoder(TestShapeEncoder):

    def test_encoder(self, ellipse):
        encoder = get_encoder(ellipse.__class__)
        v = encoder.encode(ellipse)
        self.assert_ellipse(v)


class TestRectangeEncoder(TestShapeEncoder):

    def test_encoder(self, rectangle):
        encoder = get_encoder(rectangle.__class__)
        v = encoder.encode(rectangle)
        self.assert_rectangle(v)


class TestPointEncoder(TestShapeEncoder):

    def test_encoder(self, point):
        encoder = get_encoder(point.__class__)
        v = encoder.encode(point)
        self.assert_shape(v)
        assert v['@id'] == 3L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'
        assert v['X'] == 1.0
        assert v['Y'] == 2.0


class TestPolylineEncoder(TestShapeEncoder):

    def test_encoder(self, polyline):
        encoder = get_encoder(polyline.__class__)
        v = encoder.encode(polyline)
        self.assert_shape(v)
        assert v['@id'] == 4L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polyline'
        assert v['Points'] == '0,0 1,2 3,5'


class TestPolygonEncoder(TestShapeEncoder):

    def test_encoder(self, polygon):
        encoder = get_encoder(polygon.__class__)
        v = encoder.encode(polygon)
        self.assert_shape(v)
        assert v['@id'] == 5L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polygon'
        assert v['Points'] == '0,0 1,2 3,5'


class TestRoiEncoder(TestShapeEncoder):

    def test_roi_with_shapes(self, roi_with_shapes):
        encoder = get_encoder(roi_with_shapes.__class__)
        v = encoder.encode(roi_with_shapes)
        self.assert_roi(v)
        assert len(v['shapes']) == 2
        ellipse, rectangle = v['shapes']
        self.assert_ellipse(ellipse)
        self.assert_rectangle(rectangle)
