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

import pytest

from omero.model import EllipseI, RectI, PointI, PolylineI, PolygonI
from omero.rtypes import rlong, rint, rstring, rdouble, rbool
from omero_marshal import get_encoder


def populate_shape(o):
    o.fillColor = rint(0xffffffff)
    o.fillRule = rstring('solid')
    o.fontFamily = rstring('cursive')
    o.fontSize = rint(12)
    o.fontStyle = rstring('italic')
    o.locked = rbool(False)
    o.strokeColor = rint(0xffff0000)
    o.strokeDashArray = rstring('inherit')
    o.strokeLineCap = rstring('round')
    o.strokeWidth = rint(4)
    o.textValue = rstring('the_text')
    o.theC = rint(1)
    o.theT = rint(2)
    o.theZ = rint(3)
    o.visibility = rbool(True)
    o.id = rlong(1L)
    return o


@pytest.fixture()
def ellipse():
    o = EllipseI()
    populate_shape(o)
    o.cx = rdouble(1.0)
    o.cy = rdouble(2.0)
    o.rx = rdouble(3.0)
    o.ry = rdouble(4.0)
    return o


@pytest.fixture()
def rectangle():
    o = RectI()
    populate_shape(o)
    o.x = rdouble(1.0)
    o.y = rdouble(2.0)
    o.width = rdouble(3.0)
    o.height = rdouble(4.0)
    return o


@pytest.fixture()
def point():
    o = PointI()
    populate_shape(o)
    o.cx = rdouble(1.0)
    o.cy = rdouble(2.0)
    return o


@pytest.fixture()
def polyline():
    o = PolylineI()
    populate_shape(o)
    o.points = rstring('0,0 1,2 3,5')
    return o


@pytest.fixture()
def polygon():
    o = PolygonI()
    populate_shape(o)
    o.points = rstring('0,0 1,2 3,5')
    return o


class TestShapeEncoder(object):

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


class TestEllipseEncoder(TestShapeEncoder):

    def test_encoder(self, ellipse):
        encoder = get_encoder(ellipse.__class__)()
        v = encoder.encode(ellipse)
        self.assert_shape(v)
        assert v['@id'] == 1L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'
        assert v['X'] == 1.0
        assert v['Y'] == 2.0
        assert v['RadiusX'] == 3.0
        assert v['RadiusY'] == 4.0


class TestRectangeEncoder(TestShapeEncoder):

    def test_encoder(self, rectangle):
        encoder = get_encoder(rectangle.__class__)()
        v = encoder.encode(rectangle)
        self.assert_shape(v)
        assert v['@id'] == 1L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Rectangle'
        assert v['X'] == 1.0
        assert v['Y'] == 2.0
        assert v['Width'] == 3.0
        assert v['Height'] == 4.0


class TestPointEncoder(TestShapeEncoder):

    def test_encoder(self, point):
        encoder = get_encoder(point.__class__)()
        v = encoder.encode(point)
        self.assert_shape(v)
        assert v['@id'] == 1L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'
        assert v['X'] == 1.0
        assert v['Y'] == 2.0


class TestPolylineEncoder(TestShapeEncoder):

    def test_encoder(self, polyline):
        encoder = get_encoder(polyline.__class__)()
        v = encoder.encode(polyline)
        self.assert_shape(v)
        assert v['@id'] == 1L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polyline'
        assert v['Points'] == '0,0 1,2 3,5'


class TestPolygonEncoder(TestShapeEncoder):

    def test_encoder(self, polygon):
        encoder = get_encoder(polygon.__class__)()
        v = encoder.encode(polygon)
        self.assert_shape(v)
        assert v['@id'] == 1L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Polygon'
        assert v['Points'] == '0,0 1,2 3,5'
