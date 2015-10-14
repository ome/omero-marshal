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


class TestBaseEncoder(object):

    def roi_data(self):
        return {
            '@id': 1L,
            '@type': 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI',
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_base_encoder(self, roi):
        encoder = get_encoder(roi.__class__)
        v = encoder.encode(roi)
        assert v == self.roi_data()

    def test_base_encoder_with_annotations(self, roi_with_annotations):
        encoder = get_encoder(roi_with_annotations.__class__)
        v = encoder.encode(roi_with_annotations)
        roi_data = self.roi_data()
        roi_data.update({
            'annotations': [{
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
        })
        assert v == roi_data


class TestDetailsEncoder(object):

    def experimenter_json(self):
        return {
            '@id': 1L,
            '@type':
                'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                '#Experimenter',
            'FirstName': 'the_firstName',
            'MiddleName': 'the_middleName',
            'LastName': 'the_lastName',
            'Email': 'the_email',
            'Institution': 'the_institution',
            'UserName': 'the_omeName',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_experimenter_encoder(self, experimenter):
        encoder = get_encoder(experimenter.__class__)
        v = encoder.encode(experimenter)
        assert v == self.experimenter_json()

    def experimenter_group_json(self):
        return {
            '@id': 1L,
            '@type':
                'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                '#ExperimenterGroup',
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_experimenter_group_encoder(self, experimenter_group):
        encoder = get_encoder(experimenter_group.__class__)
        v = encoder.encode(experimenter_group)
        assert v == self.experimenter_group_json()

    def permissions_json(self):
        return {
            '@type': 'TBD#Permissions',
            'perm': 'rwrwrw',
            'canAnnotate': True,
            'canDelete': True,
            'canEdit': True,
            'canLink': True
        }

    def test_permissions_encoder(self, permissions):
        encoder = get_encoder(permissions.__class__)
        v = encoder.encode(permissions)
        assert v == self.permissions_json()

    def test_details_encoder(self, details):
        encoder = get_encoder(details.__class__)
        v = encoder.encode(details)
        assert v == {
            '@type': 'TBD#Details',
            'permissions': self.permissions_json(),
            'owner': self.experimenter_json(),
            'group': self.experimenter_group_json()
        }
