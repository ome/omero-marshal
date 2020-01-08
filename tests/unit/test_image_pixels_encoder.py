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
            '@id': 1,
            '@type': '%s#Image' % OME_SCHEMA_URL,
            'AcquisitionDate': 1,
            'Name': 'image_name_1',
            'omero:archived': False,
            'Description': 'image_description_1',
            'omero:partial': False,
            'omero:series': 0,
            'omero:format': {
                '@id': 1,
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
            '@id': 1,
            '@type': '%s#Image' % OME_SCHEMA_URL,
            'AcquisitionDate': 1,
            'Name': 'image_name_1',
            'omero:archived': False,
            'Description': 'image_description_1',
            'omero:partial': False,
            'omero:series': 0,
            'omero:format': {
                '@id': 1,
                '@type': 'TBD#Format',
                'value': 'PNG',
                'omero:details': {'@type': 'TBD#Details'},
            },
            'Pixels': {
                '@id': 1,
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
                'TimeIncrement': {
                    '@type': 'TBD#TimeI',
                    'Unit': 'MILLISECOND',
                    'Symbol': 'ms',
                    'Value': 1.0
                },
                'omero:waveIncrement': 2.0,
                'omero:waveStart': 1,
                'DimensionOrder': {
                    '@id': 1,
                    '@type': 'TBD#DimensionOrder',
                    'value': 'XYZCT',
                    'omero:details': {'@type': 'TBD#Details'}
                },
                'Type': {
                    '@id': 1,
                    '@type': 'TBD#PixelsType',
                    'value': 'bit',
                    'omero:details': {'@type': 'TBD#Details'}
                },
                'Channels': [{
                    '@id': 1,
                    '@type': '%s#Channel' % OME_SCHEMA_URL,
                    'AcquisitionMode': {
                        '@id': 1,
                        '@type': 'TBD#AcquisitionMode',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'WideField'
                    },
                    'Color': -1,
                    'ContrastMethod': {
                        '@id': 8,
                        '@type': 'TBD#ContrastMethod',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'Fluorescence'
                    },
                    'EmissionWavelength': {
                        '@type': 'TBD#LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 509.0
                    },
                    'ExcitationWavelength': {
                        '@type': 'TBD#LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 488.0
                    },
                    'Fluor': 'GFP',
                    'Illumination': {
                        '@id': 1,
                        '@type': 'TBD#Illumination',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'Transmitted'
                    },
                    'NDFilter': 1.0,
                    'Name': 'GFP/488',
                    'PinholeSize': {
                        '@type': 'TBD#LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 1.0
                    },
                    'PockelCellSetting': 0,
                    'SamplesPerPixel': 2,
                    'omero:LogicalChannelId': 1,
                    'omero:details': {'@type': 'TBD#Details'},
                    'omero:lookupTable': 'rainbow',
                    'omero:photometricInterpretation': {
                        '@id': 1,
                        '@type': 'TBD#PhotometricInterpretation',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'RGB'
                    }
                }, {
                    '@id': 2,
                    '@type': '%s#Channel' % OME_SCHEMA_URL,
                    'AcquisitionMode': {
                        '@id': 1,
                        '@type': 'TBD#AcquisitionMode',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'WideField'
                    },
                    'Color': -16711681,
                    'ContrastMethod': {
                        '@id': 8,
                        '@type': 'TBD#ContrastMethod',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'Fluorescence'
                    },
                    'EmissionWavelength': {
                        '@type': 'TBD#LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 470.0
                    },
                    'ExcitationWavelength': {
                        '@type': 'TBD#LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 405.0
                    },
                    'Fluor': 'DAPI',
                    'Illumination': {
                        '@id': 1,
                        '@type': 'TBD#Illumination',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'Transmitted'
                    },
                    'NDFilter': 1.0,
                    'Name': 'DAPI/405',
                    'PinholeSize': {
                        '@type': 'TBD#LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 2.0
                    },
                    'PockelCellSetting': 0,
                    'SamplesPerPixel': 2,
                    'omero:LogicalChannelId': 2,
                    'omero:details': {'@type': 'TBD#Details'},
                    'omero:lookupTable': 'rainbow',
                    'omero:photometricInterpretation': {
                        '@id': 1,
                        '@type': 'TBD#PhotometricInterpretation',
                        'omero:details': {'@type': 'TBD#Details'},
                        'value': 'RGB'
                    }
                }],
                'omero:details': {'@type': 'TBD#Details'}
            },
            'omero:details': {'@type': 'TBD#Details'}
        }
