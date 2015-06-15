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

from omero.model import RoiI, EllipseI, RectI, PointI, PolylineI, PolygonI
from omero.rtypes import rlong, rint, rstring, rdouble, rbool


@pytest.fixture()
def roi():
    o = RoiI()
    o.id = rlong(1L)
    o.description = rstring('the_name')
    return o


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
