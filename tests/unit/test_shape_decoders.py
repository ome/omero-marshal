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
from omero.model.enums import UnitsLength
from omero.rtypes import RDoubleI, RStringI
from omero.model import LengthI


class TestShapeDecoder(object):

    def assert_experimenter(self, experimenter):
        assert experimenter.id.val == 1
        assert experimenter.email.val == 'the_email'
        assert experimenter.firstName.val == 'the_firstName'
        assert experimenter.lastName.val == 'the_lastName'
        assert experimenter.middleName.val == 'the_middleName'
        assert experimenter.omeName.val == 'the_omeName'

    def assert_experimenter_group(self, experimenter_group):
        assert experimenter_group.id.val == 1
        assert experimenter_group.name.val == 'the_name'
        assert experimenter_group.description.val == 'the_description'

    def assert_permissions(self, permissions):
        assert str(permissions) == 'rwrwrw'

    def assert_externalInfo(self, externalInfo):
        assert externalInfo.entityId.val == 123
        assert externalInfo.entityType.val == 'test'
        assert externalInfo.lsid.val == 'ABCDEF'
        assert externalInfo.uuid.val == 'f90a1fd5-275c-4d14-82b3-87b5ef0f07de'

    def assert_details(self, details):
        self.assert_experimenter(details.owner)
        self.assert_experimenter_group(details.group)
        self.assert_permissions(details.permissions)
        self.assert_externalInfo(details.externalInfo)

    def assert_annotations(self, o):
        assert o.annotationLinksLoaded
        boolean_annotation, comment_annotation, double_annotation, \
            long_annotation, map_annotation, tag_annotation, \
            term_annotation, timestamp_annotation, xml_annotation = \
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
        assert long_annotation.longValue.val == 1
        assert map_annotation.ns.val == 'map_annotation'
        assert map_annotation.description.val == 'the_description'
        map_value_a, map_value_b = map_annotation.getMapValue()
        assert map_value_a.name == 'a'
        assert map_value_a.value == '1'
        assert map_value_b.name == 'b'
        assert map_value_b.value == '2'
        assert tag_annotation.ns.val == 'tag_annotation'
        assert tag_annotation.description.val == 'the_description'
        assert tag_annotation.textValue.val == 'tag_value'
        assert term_annotation.ns.val == 'term_annotation'
        assert term_annotation.description.val == 'the_description'
        assert term_annotation.termValue.val == 'term_value'
        assert timestamp_annotation.ns.val == 'timestamp_annotation'
        assert timestamp_annotation.description.val == 'the_description'
        assert timestamp_annotation.timeValue.val == 1

    def assert_roi(self, roi, has_annotations=False):
        assert roi.id.val == 1
        assert roi.description.val == 'the_description'
        assert roi.name.val == 'the_name'
        if not has_annotations:
            assert not roi.annotationLinksLoaded
        else:
            self.assert_annotations(roi)
        self.assert_details(roi.details)

    def assert_shape(self, shape, has_annotations=False,
                     has_unit_information=True):
        assert shape.fillColor.val == 0xffffffff
        assert shape.fillRule.val == 'solid'
        assert shape.strokeColor.val == 0xffff0000
        assert shape.strokeDashArray.val == 'inherit'
        if has_unit_information:
            assert shape.strokeWidth.__class__ is LengthI
            assert shape.strokeWidth.getUnit() == UnitsLength.PIXEL
            assert shape.strokeWidth.getValue() == 4
        else:
            assert shape.strokeWidth is None
        assert shape.textValue.val == 'the_text'
        assert shape.fontFamily.val == 'cursive'
        if has_unit_information:
            assert shape.fontSize.__class__ is LengthI
            assert shape.fontSize.getUnit() == UnitsLength.POINT
            assert shape.fontSize.getValue() == 12
        else:
            assert shape.fontSize is None
        assert shape.fontStyle.val == 'italic'
        if SCHEMA_VERSION == '2015-01':
            assert shape.visibility.val is True
            assert shape.strokeLineCap.val == 'round'
        assert shape.locked.val is False
        assert shape.theZ.val == 3
        assert shape.theT.val == 2
        assert shape.theC.val == 1
        if SCHEMA_VERSION == '2015-01':
            assert shape.transform.__class__ is RStringI
            assert shape.transform.val == 'matrix(1.0 0.0 0.0 1.0 0.0 0.0)'
        else:
            from omero.model import AffineTransformI
            assert shape.transform.__class__ is AffineTransformI
            assert shape.transform.getA00().val == 1.0
            assert shape.transform.getA10().val == 0.0
            assert shape.transform.getA01().val == 0.0
            assert shape.transform.getA11().val == 1.0
            assert shape.transform.getA02().val == 0.0
            assert shape.transform.getA12().val == 0.0
        if not has_annotations:
            assert not shape.annotationLinksLoaded
        else:
            self.assert_annotations(shape)

    def assert_ellipse(self, ellipse, has_annotations=False):
        self.assert_shape(ellipse, has_annotations=has_annotations)
        assert ellipse.id.val == 1
        if SCHEMA_VERSION == '2016-06':
            assert ellipse.x.__class__ is RDoubleI
            assert ellipse.x.val == 1.0
            assert ellipse.y.__class__ is RDoubleI
            assert ellipse.y.val == 2.0
            assert ellipse.radiusX.__class__ is RDoubleI
            assert ellipse.radiusX.val == 3.0
            assert ellipse.radiusY.__class__ is RDoubleI
            assert ellipse.radiusY.val == 4.0
        else:
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
        assert rectangle.id.val == 2
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

    def test_encoder_with_annotations(self, ellipse_with_annotations):
        encoder = get_encoder(ellipse_with_annotations.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(ellipse_with_annotations)
        v = decoder.decode(v)
        self.assert_ellipse(v, has_annotations=True)


class TestRectangleDecoder(TestShapeDecoder):

    def test_decoder(self, rectangle):
        encoder = get_encoder(rectangle.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(rectangle)
        v = decoder.decode(v)
        self.assert_rectangle(v)


class TestPointDecoder(TestShapeDecoder):

    def test_decoder(self, point):
        encoder = get_encoder(point.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(point)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 3
        if SCHEMA_VERSION == '2016-06':
            assert v.x.__class__ is RDoubleI
            assert v.x.val == 1.0
            assert v.y.__class__ is RDoubleI
            assert v.y.val == 2.0
        else:
            assert v.cx.__class__ is RDoubleI
            assert v.cx.val == 1.0
            assert v.cy.__class__ is RDoubleI
            assert v.cy.val == 2.0


class TestLabelDecoder(TestShapeDecoder):

    def test_decoder(self, label):
        encoder = get_encoder(label.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(label)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 7
        assert v.x.__class__ is RDoubleI
        assert v.x.val == 1.0
        assert v.y.__class__ is RDoubleI
        assert v.y.val == 2.0


class TestLineDecoder(TestShapeDecoder):

    def test_decoder(self, line):
        encoder = get_encoder(line.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(line)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 6
        assert v.x1.__class__ is RDoubleI
        assert v.x1.val == 0.0
        assert v.y1.__class__ is RDoubleI
        assert v.y1.val == 0.0
        assert v.x2.__class__ is RDoubleI
        assert v.x2.val == 1.0
        assert v.y2.__class__ is RDoubleI
        assert v.y2.val == 2.0
        if SCHEMA_VERSION != '2015-01':
            assert v.markerStart.val == 'Arrow'
            assert v.markerEnd.val == 'Arrow'


class TestPolylineDecoder(TestShapeDecoder):

    def test_decoder(self, polyline):
        encoder = get_encoder(polyline.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(polyline)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 4
        assert v.points.val == '0,0 1,2 3,5'
        if SCHEMA_VERSION != '2015-01':
            assert v.markerStart.val == 'Arrow'
            assert v.markerEnd.val == 'Arrow'


class TestPolygonDecoder(TestShapeDecoder):

    def test_decoder(self, polygon):
        encoder = get_encoder(polygon.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(polygon)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 5
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


class TestOptionalUnitInformation(TestShapeDecoder):

    def test_decoder(self, opt_unit_label):
        encoder = get_encoder(opt_unit_label.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(opt_unit_label)
        v = decoder.decode(v)
        self.assert_shape(v, has_unit_information=False)
        assert v.id.val == 7
        assert v.x.__class__ is RDoubleI
        assert v.x.val == 1.0
        assert v.y.__class__ is RDoubleI
        assert v.y.val == 2.0


class TestMaskDecoder(TestShapeDecoder):

    def test_decoder(self, mask):
        encoder = get_encoder(mask.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(mask)
        v = decoder.decode(v)
        self.assert_shape(v)
        assert v.id.val == 8
