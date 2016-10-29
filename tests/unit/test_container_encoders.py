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

    def test_project_with_datasets_encoder(self, project_with_datasets):
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

    def test_project_with_datasets_and_images_encoder(
            self, project_with_datasets_and_images):
        encoder = get_encoder(project_with_datasets_and_images.__class__)
        v = encoder.encode(project_with_datasets_and_images)
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
                'omero:details': {'@type': 'TBD#Details'},
                'Images': [{
                    '@id': 1L,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1L,
                    'Name': 'image_name_1',
                    'omero:archived': False,
                    'Description': 'image_description_1',
                    'omero:partial': False,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                }, {
                    '@id': 2L,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1L,
                    'Name': 'image_name_2',
                    'omero:archived': False,
                    'Description': 'image_description_2',
                    'omero:partial': False,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                }]
            }, {
                '@id': 2L,
                '@type': '%s#Dataset' % OME_SCHEMA_URL,
                'Name': 'dataset_name_2',
                'Description': 'dataset_description_2',
                'omero:details': {'@type': 'TBD#Details'},
                'Images': [{
                    '@id': 3L,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1L,
                    'Name': 'image_name_3',
                    'omero:archived': False,
                    'Description': 'image_description_3',
                    'omero:partial': False,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                }, {
                    '@id': 4L,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1L,
                    'Name': 'image_name_4',
                    'omero:archived': False,
                    'Description': 'image_description_4',
                    'omero:partial': False,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                }]
            }]
        }
