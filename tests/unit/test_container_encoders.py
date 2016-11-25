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
                    'omero:series': 0L,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 2L,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1L,
                    'Name': 'image_name_2',
                    'omero:archived': False,
                    'Description': 'image_description_2',
                    'omero:partial': False,
                    'omero:series': 0L,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                    'omero:details': {'@type': 'TBD#Details'}
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
                    'omero:series': 0L,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 4L,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1L,
                    'Name': 'image_name_4',
                    'omero:archived': False,
                    'Description': 'image_description_4',
                    'omero:partial': False,
                    'omero:series': 0L,
                    'omero:format': {
                        '@id': 1L,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                    'omero:details': {'@type': 'TBD#Details'}
                }]
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
                'FieldIndex': 0,
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
                'Wells': [{
                    '@id': 7L,
                    '@type': '%s#Well' % OME_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_7',
                    'ExternalIdentifier': 'external_identifier_7',
                    'Type': 'the_type',
                    'Alpha': 0,
                    'Red': 255,
                    'Green': 0,
                    'Blue': 0,
                    'omero:status': 'the_status',
                    'WellSamples': [{
                        '@id': 9L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 8L,
                    '@type': '%s#Well' % OME_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_8',
                    'ExternalIdentifier': 'external_identifier_8',
                    'Type': 'the_type',
                    'Alpha': 0,
                    'Red': 255,
                    'Green': 0,
                    'Blue': 0,
                    'omero:status': 'the_status',
                                        'WellSamples': [{
                        '@id': 9L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }],
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
                'FieldIndex': 0,
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
                'Wells': [{
                    '@id': 7L,
                    '@type': '%s#Well' % OME_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_7',
                    'ExternalIdentifier': 'external_identifier_7',
                    'Type': 'the_type',
                    'Alpha': 0,
                    'Red': 255,
                    'Green': 0,
                    'Blue': 0,
                    'omero:status': 'the_status',
                    'WellSamples': [{
                        '@id': 9L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 8L,
                    '@type': '%s#Well' % OME_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_8',
                    'ExternalIdentifier': 'external_identifier_8',
                    'Type': 'the_type',
                    'Alpha': 0,
                    'Red': 255,
                    'Green': 0,
                    'Blue': 0,
                    'omero:status': 'the_status',
                                        'WellSamples': [{
                        '@id': 9L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10L,
                        '@type': '%s#WellSample' % OME_SCHEMA_URL,
                        'PositionX': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 1.0
                        },
                        'PositionY': {
                            '@type': 'TBD#LengthI',
                            'Unit': 'REFERENCEFRAME',
                            'Symbol': 'reference frame',
                            'Value': 2.0
                        },
                        'Timepoint': 1L,
                        'Image': {
                            '@id': 1L,
                            '@type': '%s#Image' % OME_SCHEMA_URL,
                            'AcquisitionDate': 1L,
                            'Name': 'image_name_1',
                            'omero:archived': False,
                            'Description': 'image_description_1',
                            'omero:partial': False,
                            'omero:series': 0,
                            'omero:format': {
                                '@id': 1L,
                                '@type': 'TBD#Format',
                                'value': 'PNG',
                                'omero:details': {'@type': 'TBD#Details'},
                            },
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }],
                'omero:details': {'@type': 'TBD#Details'}
            }]
        }
