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

class TestImagePixelsEncoder(object):

    def test_image_encoder(self, image, contexts):
        encoder = get_encoder(image.__class__)
        v = encoder.encode(image, True)
        assert v == {
            **contexts,
            '@id': 1,
            '@type': 'Image',
            'AcquisitionDate': 1,
            'Name': 'image_name_1',
            'omero:archived': False,
            'Description': 'image_description_1',
            'omero:partial': False,
            'omero:series': 0,
            'omero:format': {
                '@id': 1,
                '@type': 'omero:Format',
                'value': 'PNG',
                'omero:details': {'@type': 'omero:Details'},
            },
            'omero:details': {'@type': 'omero:Details'}
        }

    def test_image_pixels_encoder(self, image_pixels, contexts):
        encoder = get_encoder(image_pixels.__class__)
        v = encoder.encode(image_pixels, True)
        assert v == {
            **contexts,
            '@id': 1,
            '@type': 'Image',
            'AcquisitionDate': 1,
            'Name': 'image_name_1',
            'omero:archived': False,
            'Description': 'image_description_1',
            'omero:partial': False,
            'omero:series': 0,
            'omero:format': {
                '@id': 1,
                '@type': 'omero:Format',
                'value': 'PNG',
                'omero:details': {'@type': 'omero:Details'},
            },
            'Pixels': {
                '@id': 1,
                '@type': 'Pixels',
                'omero:methodology': 'methodology',
                'PhysicalSizeX': {
                    '@type': 'omero:LengthI',
                    'Unit': 'MICROMETER',
                    'Symbol': 'µm',
                    'Value': 1.0
                },
                'PhysicalSizeY': {
                    '@type': 'omero:LengthI',
                    'Unit': 'MICROMETER',
                    'Symbol': 'µm',
                    'Value': 2.0
                },
                'PhysicalSizeZ': {
                    '@type': 'omero:LengthI',
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
                    '@type': 'omero:TimeI',
                    'Unit': 'MILLISECOND',
                    'Symbol': 'ms',
                    'Value': 1.0
                },
                'omero:waveIncrement': 2.0,
                'omero:waveStart': 1,
                'DimensionOrder': {
                    '@id': 1,
                    '@type': 'DimensionOrder',
                    'value': 'XYZCT',
                    'omero:details': {'@type': 'omero:Details'}
                },
                'Type': {
                    '@id': 1,
                    '@type': 'PixelType',
                    'value': 'bit',
                    'omero:details': {'@type': 'omero:Details'}
                },
                'Channels': [{
                    '@id': 1,
                    '@type': 'Channel',
                    'AcquisitionMode': {
                        '@id': 1,
                        '@type': 'AcquisitionMode',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'WideField'
                    },
                    'Color': -1,
                    'ContrastMethod': {
                        '@id': 8,
                        '@type': 'ContrastMethod',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'Fluorescence'
                    },
                    'EmissionWavelength': {
                        '@type': 'omero:LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 509.0
                    },
                    'ExcitationWavelength': {
                        '@type': 'omero:LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 488.0
                    },
                    'Fluor': 'GFP',
                    'Illumination': {
                        '@id': 1,
                        '@type': 'IlluminationType',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'Transmitted'
                    },
                    'NDFilter': 1.0,
                    'Name': 'GFP/488',
                    'PinholeSize': {
                        '@type': 'omero:LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 1.0
                    },
                    'PockelCellSetting': 0,
                    'SamplesPerPixel': 2,
                    'omero:LogicalChannelId': 1,
                    'omero:details': {'@type': 'omero:Details'},
                    'omero:lookupTable': 'rainbow',
                    'omero:photometricInterpretation': {
                        '@id': 1,
                        '@type': 'omero:PhotometricInterpretation',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'RGB'
                    }
                }, {
                    '@id': 2,
                    '@type': 'Channel',
                    'AcquisitionMode': {
                        '@id': 1,
                        '@type': 'AcquisitionMode',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'WideField'
                    },
                    'Color': -16711681,
                    'ContrastMethod': {
                        '@id': 8,
                        '@type': 'ContrastMethod',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'Fluorescence'
                    },
                    'EmissionWavelength': {
                        '@type': 'omero:LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 470.0
                    },
                    'ExcitationWavelength': {
                        '@type': 'omero:LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 405.0
                    },
                    'Fluor': 'DAPI',
                    'Illumination': {
                        '@id': 1,
                        '@type': 'IlluminationType',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'Transmitted'
                    },
                    'NDFilter': 1.0,
                    'Name': 'DAPI/405',
                    'PinholeSize': {
                        '@type': 'omero:LengthI',
                        'Symbol': 'nm',
                        'Unit': 'NANOMETER',
                        'Value': 2.0
                    },
                    'PockelCellSetting': 0,
                    'SamplesPerPixel': 2,
                    'omero:LogicalChannelId': 2,
                    'omero:details': {'@type': 'omero:Details'},
                    'omero:lookupTable': 'rainbow',
                    'omero:photometricInterpretation': {
                        '@id': 1,
                        '@type': 'omero:PhotometricInterpretation',
                        'omero:details': {'@type': 'omero:Details'},
                        'value': 'RGB'
                    }
                }],
                'omero:details': {'@type': 'omero:Details'}
            },
            'omero:details': {'@type': 'omero:Details'}
        }
