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

from omero_marshal import get_encoder, OME_SCHEMA_URL


class TestProjectEncoder(object):

    def test_project_encoder(self, project):
        encoder = get_encoder(project.__class__)
        v = encoder.encode(project)
        assert v == {
            '@id': 1L,
            '@type': '%s#Project' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_project_with_dataset_encoder(self, project_with_datasets):
        encoder = get_encoder(project_with_datasets.__class__)
        v = encoder.encode(project_with_datasets)
        assert v == {
            '@id': 1L,
            '@type': '%s#Project' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'},
            'Datasets': [{
                '@id': 1L,
                '@type': '%s#Dataset' % OME_SCHEMA_URL,
                'Name': 'dataset_name_1',
                'Description': 'dataset_description_1',
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@id': 2L,
                '@type': '%s#Dataset' % OME_SCHEMA_URL,
                'Name': 'dataset_name_2',
                'Description': 'dataset_description_2',
                'omero:details': {'@type': 'TBD#Details'}
            }]
        }


class TestScreenEncoder(object):

    def test_screen_encoder(self, screen):
        encoder = get_encoder(screen.__class__)
        v = encoder.encode(screen)
        assert v == {
            '@id': 4L,
            '@type': '%s#Screen' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'ProtocolDescription': 'the_protocol_description',
            'ProtocolIdentifier': 'the_protocol_identifier',
            'ReagentSetDescription': 'the_reagent_set_description',
            'ReagentSetIdentifier': 'the_reagent_set_identifier',
            'Type': 'the_type',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_screen_with_plate_encoder(self, screen_with_plates):
        encoder = get_encoder(screen_with_plates.__class__)
        v = encoder.encode(screen_with_plates)
        assert v == {
            '@id': 4L,
            '@type': '%s#Screen' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'ProtocolDescription': 'the_protocol_description',
            'ProtocolIdentifier': 'the_protocol_identifier',
            'ReagentSetDescription': 'the_reagent_set_description',
            'ReagentSetIdentifier': 'the_reagent_set_identifier',
            'Type': 'the_type',
            'omero:details': {'@type': 'TBD#Details'},
            'Plates': [{
                '@id': 5L,
                '@type': '%s#Plate' % OME_SCHEMA_URL,
                'Name': 'plate_name_5',
                'Description': 'plate_description_5',
                'ColumnNamingConvention': 'number',
                'RowNamingConvention': 'letter',
                'Columns': 12,
                'Rows': 8,
                'FieldIndex': 'default_sample_5',
                'ExternalIdentifier': 'external_identifier_5',
                'Status': 'status_5',
                'WellOriginX': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'REFERENCEFRAME',
                    'Symbol': 'reference frame',
                    'Value': 0.1
                },
                'WellOriginY': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'REFERENCEFRAME',
                    'Symbol': 'reference frame',
                    'Value': 1.1
                },
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@id': 6L,
                '@type': '%s#Plate' % OME_SCHEMA_URL,
                'Name': 'plate_name_6',
                'Description': 'plate_description_6',
                'ColumnNamingConvention': 'number',
                'RowNamingConvention': 'letter',
                'Columns': 12,
                'Rows': 8,
                'FieldIndex': 'default_sample_6',
                'ExternalIdentifier': 'external_identifier_6',
                'Status': 'status_6',
                'WellOriginX': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'REFERENCEFRAME',
                    'Symbol': 'reference frame',
                    'Value': 0.1
                },
                'WellOriginY': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'REFERENCEFRAME',
                    'Symbol': 'reference frame',
                    'Value': 1.1
                },
                'omero:details': {'@type': 'TBD#Details'}
            }]
        }
