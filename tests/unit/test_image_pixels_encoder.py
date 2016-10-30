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


class TestImagePixelsEncoder(object):

    def test_image_encoder(self, image):
        encoder = get_encoder(image.__class__)
        v = encoder.encode(image)
        assert v == {
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
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_image_pixels_encoder(self, image_pixels):
        encoder = get_encoder(image_pixels.__class__)
        v = encoder.encode(image_pixels)
        assert v == {
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
            'Pixels': {
                '@id': 1L,
                '@type': '%s#Pixels' % OME_SCHEMA_URL,
                'omero:methodology': 'methodology',
                'PhysicalSizeX': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'MICROMETER',
                    'Symbol': 'µm',
                    'Value': 1.0
                },
                'PhysicalSizeY': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'MICROMETER',
                    'Symbol': 'µm',
                    'Value': 2.0
                },
                'PhysicalSizeZ': {
                    '@type': 'TBD#LengthI',
                    'Unit': 'MICROMETER',
                    'Symbol': 'µm',
                    'Value': 3.0
                },
                'omero:sha1': '61ee8b5601a84d5154387578466c8998848ba089',
                'SignificantBits': 16,
                'SizeX': 1,
                'SizeY': 2,
                'SizeZ': 3,
                'SizeC': 4,
                'SizeT': 5,
                'TimeIncrement': 1.0,
                'omero:waveIncrement': 2.0,
                'omero:waveStart': 1,
                'DimensionOrder': 'XYZCT',
                'Type': 'bit',
                'omero:details': {'@type': 'TBD#Details'}
            },
            'omero:details': {'@type': 'TBD#Details'}
        }
