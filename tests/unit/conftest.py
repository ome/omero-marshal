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

from omero.model import BooleanAnnotationI, CommentAnnotationI, DatasetI, \
    DoubleAnnotationI, LongAnnotationI, MapAnnotationI, TagAnnotationI, \
    TermAnnotationI, TimestampAnnotationI, XmlAnnotationI, RoiI, EllipseI, \
    RectI, PointI, PolylineI, PolygonI, ProjectI, ExperimenterI, \
    ExperimenterGroupI, PermissionsI, DetailsI, LengthI, NamedValue
from omero.model.enums import UnitsLength
from omero.rtypes import rlong, rint, rstring, rdouble, rbool, rtime


@pytest.fixture()
def project():
    o = ProjectI()
    o.id = rlong(1L)
    o.name = rstring('the_name')
    o.description = rstring('the_description')
    return o


@pytest.fixture()
def project_with_datasets(project):
    for dataset_id in range(1, 3):
        o = DatasetI()
        o.id = rlong(dataset_id)
        o.name = rstring('dataset_name_%d' % dataset_id)
        o.description = rstring('dataset_description_%d' % dataset_id)
        project.linkDataset(o)
    return project


def add_annotations(o):
    '''
    Annotation
        BasicAnnotation
            BooleanAnnotation
                BooleanAnnotationI
            NumericAnnotation
                DoubleAnnotation
                    DoubleAnnotationI
                LongAnnotation
                    LongAnnotationI
            TermAnnotation
                TermAnnotationI
            TimestampAnnotation
                TimestampAnnotationI
        ListAnnotation
            ListAnnotationI
        MapAnnotation
            MapAnnotationI
        TextAnnotation
            CommentAnnotation
                CommentAnnotationI
            TagAnnotation
                TagAnnotationI
            XmlAnnotation
                XmlAnnotationI
        TypeAnnotation
            FileAnnotation
                FileAnnotationI
    '''
    annotation = BooleanAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('boolean_annotation')
    annotation.boolValue = rbool(True)
    o.linkAnnotation(annotation)
    annotation = CommentAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('comment_annotation')
    annotation.textValue = rstring('text_value')
    o.linkAnnotation(annotation)
    annotation = DoubleAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('double_annotation')
    annotation.doubleValue = rdouble(1.0)
    o.linkAnnotation(annotation)
    annotation = LongAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('long_annotation')
    annotation.longValue = rlong(1L)
    o.linkAnnotation(annotation)
    annotation = MapAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('map_annotation')
    annotation.setMapValue([NamedValue('a', '1'), NamedValue('b', '2')])
    o.linkAnnotation(annotation)
    annotation = TagAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('tag_annotation')
    annotation.textValue = rstring('tag_value')
    o.linkAnnotation(annotation)
    annotation = TermAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('term_annotation')
    annotation.termValue = rstring('term_value')
    o.linkAnnotation(annotation)
    annotation = TimestampAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('timestamp_annotation')
    annotation.timeValue = rtime(1)
    o.linkAnnotation(annotation)
    annotation = XmlAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('xml_annotation')
    annotation.textValue = rstring('<xml_value></xml_value>')
    o.linkAnnotation(annotation)


@pytest.fixture()
def experimenter():
    o = ExperimenterI()
    o.id = rlong(1L)
    o.email = rstring('the_email')
    o.firstName = rstring('the_firstName')
    o.institution = rstring('the_institution')
    o.lastName = rstring('the_lastName')
    o.middleName = rstring('the_middleName')
    o.omeName = rstring('the_omeName')
    return o


@pytest.fixture()
def experimenter_group():
    o = ExperimenterGroupI()
    o.id = rlong(1L)
    o.name = rstring('the_name')
    o.description = rstring('the_description')
    return o


@pytest.fixture()
def permissions():
    o = PermissionsI()
    return o


@pytest.fixture()
def permissions_cannot_link(permissions):
    permissions._restrictions = [True, False, False, False]
    return permissions


@pytest.fixture()
def permissions_cannot_edit(permissions):
    permissions._restrictions = [False, True, False, False]
    return permissions


@pytest.fixture()
def permissions_cannot_delete(permissions):
    permissions._restrictions = [False, False, True, False]
    return permissions


@pytest.fixture()
def permissions_cannot_annotate(permissions):
    permissions._restrictions = [False, False, False, True]
    return permissions


@pytest.fixture()
def details(experimenter, experimenter_group, permissions):
    o = DetailsI()
    o.owner = experimenter
    o.group = experimenter_group
    o.permissions = permissions
    return o


@pytest.fixture()
def roi(experimenter, experimenter_group, permissions):
    o = RoiI()
    o.id = rlong(1L)
    o.name = rstring('the_name')
    o.description = rstring('the_description')
    o.details.owner = experimenter
    o.details.group = experimenter_group
    o.details.permissions = permissions
    return o


@pytest.fixture()
def roi_with_unloaded_details_children(roi):
    roi.details.owner = ExperimenterI(1L, False)
    roi.details.group = ExperimenterGroupI(1L, False)
    return roi


@pytest.fixture()
def roi_with_shapes(roi, ellipse, rectangle):
    roi.addShape(ellipse)
    roi.addShape(rectangle)
    return roi


@pytest.fixture()
def roi_with_shapes_and_annotations(roi, ellipse, rectangle):
    roi.addShape(ellipse)
    roi.addShape(rectangle)
    add_annotations(roi)
    return roi


def populate_shape(o):
    o.fillColor = rint(0xffffffff)
    o.fillRule = rstring('solid')
    o.fontFamily = rstring('cursive')
    o.fontSize = LengthI(12, UnitsLength.POINT)
    o.fontStyle = rstring('italic')
    o.locked = rbool(False)
    o.strokeColor = rint(0xffff0000)
    o.strokeDashArray = rstring('inherit')
    o.strokeLineCap = rstring('round')
    o.strokeWidth = LengthI(4, UnitsLength.PIXEL)
    o.textValue = rstring('the_text')
    o.theC = rint(1)
    o.theT = rint(2)
    o.theZ = rint(3)
    o.visibility = rbool(True)
    return o


@pytest.fixture()
def ellipse():
    o = EllipseI()
    populate_shape(o)
    o.cx = rdouble(1.0)
    o.cy = rdouble(2.0)
    o.rx = rdouble(3.0)
    o.ry = rdouble(4.0)
    o.id = rlong(1L)
    return o


@pytest.fixture()
def ellipse_with_annotations():
    o = EllipseI()
    populate_shape(o)
    add_annotations(o)
    o.cx = rdouble(1.0)
    o.cy = rdouble(2.0)
    o.rx = rdouble(3.0)
    o.ry = rdouble(4.0)
    o.id = rlong(1L)
    return o


@pytest.fixture()
def rectangle():
    o = RectI()
    populate_shape(o)
    o.x = rdouble(1.0)
    o.y = rdouble(2.0)
    o.width = rdouble(3.0)
    o.height = rdouble(4.0)
    o.id = rlong(2L)
    return o


@pytest.fixture()
def point():
    o = PointI()
    populate_shape(o)
    o.cx = rdouble(1.0)
    o.cy = rdouble(2.0)
    o.id = rlong(3L)
    return o


@pytest.fixture()
def polyline():
    o = PolylineI()
    populate_shape(o)
    o.points = rstring('0,0 1,2 3,5')
    o.id = rlong(4L)
    return o


@pytest.fixture()
def polygon():
    o = PolygonI()
    populate_shape(o)
    o.points = rstring('0,0 1,2 3,5')
    o.id = rlong(5L)
    return o
