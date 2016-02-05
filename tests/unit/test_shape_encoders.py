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

    def annotation_data(self):
        return {
            'Annotations': [{
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#BooleanAnnotation',
                'Description': 'the_description',
                'Namespace': 'boolean_annotation',
                'Value': True,
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#CommentAnnotation',
                'Description': 'the_description',
                'Namespace': 'comment_annotation',
                'Value': 'text_value',
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#DoubleAnnotation',
                'Description': 'the_description',
                'Namespace': 'double_annotation',
                'Value': 1.0,
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#LongAnnotation',
                'Description': 'the_description',
                'Namespace': 'long_annotation',
                'Value': 1L,
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#MapAnnotation',
                'Description': 'the_description',
                'Namespace': 'map_annotation',
                'Value': [['a', '1'], ['b', '2']],
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#TagAnnotation',
                'Description': 'the_description',
                'Namespace': 'tag_annotation',
                'Value': 'tag_value',
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#TermAnnotation',
                'Description': 'the_description',
                'Namespace': 'term_annotation',
                'Value': 'term_value',
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#TimestampAnnotation',
                'Description': 'the_description',
                'Namespace': 'timestamp_annotation',
                'Value': 1L,
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@type': 'http://www.openmicroscopy.org/Schemas/SA/2015-01'
                         '#XmlAnnotation',
                'Description': 'the_description',
                'Namespace': 'xml_annotation',
                'Value': '<xml_value></xml_value>',
                'omero:details': {'@type': 'TBD#Details'}
            }]
        }

    def assert_annotations(self, v):
        assert v['Annotations'] == self.annotation_data()['Annotations']

    def assert_roi(self, roi, has_annotations=False):
        assert roi['@id'] == 1L
        assert roi['Name'] == 'the_name'
        assert roi['Description'] == 'the_description'
        assert roi['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'
        assert roi['omero:details'] == {
            '@type': 'TBD#Details',
            'group': {
                '@id': 1L,
                '@type':
                    'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                    '#ExperimenterGroup',
                'Description': 'the_description',
                'Name': 'the_name',
                'omero:details': {'@type': 'TBD#Details'}
            },
            'owner': {
                '@id': 1L,
                '@type':
                    'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                    '#Experimenter',
                'Email': 'the_email',
                'FirstName': 'the_firstName',
                'Institution': 'the_institution',
                'LastName': 'the_lastName',
                'MiddleName': 'the_middleName',
                'UserName': 'the_omeName',
                'omero:details': {'@type': 'TBD#Details'}
            },
            'permissions': {
                '@type': 'TBD#Permissions',
                'canAnnotate': True,
                'canDelete': True,
                'canEdit': True,
                'canLink': True,
                'perm': 'rwrwrw'
            }
        }
        if not has_annotations:
            assert roi.get('Annotations') is None
        else:
            self.assert_annotations(roi)

    def assert_shape(self, shape, has_annotations=False):
        assert shape['FillColor'] == 0xffffffff
        assert shape['FillRule'] == 'solid'
        assert shape['StrokeColor'] == 0xffff0000
        assert shape['StrokeDashArray'] == 'inherit'
        assert shape['StrokeWidth'] == {
            '@type': 'TBD#LengthI',
            'Unit': 'PIXEL',
            'Symbol': 'pixel',
            'Value': 4
        }
        assert shape['LineCap'] == 'round'
        assert shape['Text'] == 'the_text'
        assert shape['FontFamily'] == 'cursive'
        assert shape['FontSize'] == {
            '@type': 'TBD#LengthI',
            'Unit': 'POINT',
            'Symbol': 'pt',
            'Value': 12
        }
        assert shape['FontStyle'] == 'italic'
        assert shape['Visible'] is True
        assert shape['Locked'] is False
        assert shape['TheZ'] == 3
        assert shape['TheT'] == 2
        assert shape['TheC'] == 1
        assert shape['omero:details'] == {'@type': 'TBD#Details'}
        if not has_annotations:
            assert shape.get('annotations') is None
        else:
            self.assert_annotations(shape)

    def assert_ellipse(self, ellipse, has_annotations=False):
        self.assert_shape(ellipse, has_annotations=has_annotations)
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

    def test_encoder_with_annotations(self, ellipse_with_annotations):
        encoder = get_encoder(ellipse_with_annotations.__class__)
        v = encoder.encode(ellipse_with_annotations)
        self.assert_ellipse(v, has_annotations=True)


class TestRectangleEncoder(TestShapeEncoder):

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


class TestLineEncoder(TestShapeEncoder):

    def test_encoder(self, line):
        encoder = get_encoder(line.__class__)
        v = encoder.encode(line)
        self.assert_shape(v)
        assert v['@id'] == 6L
        assert v['@type'] == \
            'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Line'
        assert v['X1'] == 0.0
        assert v['Y1'] == 0.0
        assert v['X2'] == 1.0
        assert v['Y2'] == 2.0

class TestRoiEncoder(TestShapeEncoder):

    def assert_roi_with_shapes(self, v, has_annotations=False):
        self.assert_roi(v, has_annotations=has_annotations)
        assert len(v['shapes']) == 2
        ellipse, rectangle = v['shapes']
        self.assert_ellipse(ellipse)
        self.assert_rectangle(rectangle)

    def test_roi_with_shapes(self, roi_with_shapes):
        encoder = get_encoder(roi_with_shapes.__class__)
        v = encoder.encode(roi_with_shapes)
        self.assert_roi_with_shapes(v)

    def test_roi_with_shapes_and_annotations(
            self, roi_with_shapes_and_annotations):
        encoder = get_encoder(roi_with_shapes_and_annotations.__class__)
        v = encoder.encode(roi_with_shapes_and_annotations)
        self.assert_roi_with_shapes(v, has_annotations=True)
