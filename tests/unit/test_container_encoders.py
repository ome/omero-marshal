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

from omero_marshal import get_encoder, OME_SCHEMA_URL, SPW_SCHEMA_URL


class TestProjectEncoder(object):

    def test_project_encoder(self, project):
        encoder = get_encoder(project.__class__)
        v = encoder.encode(project)
        assert v == {
            '@id': 1,
            '@type': '%s#Project' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_project_with_datasets_encoder(self, project_with_datasets):
        encoder = get_encoder(project_with_datasets.__class__)
        v = encoder.encode(project_with_datasets)
        assert v == {
            '@id': 1,
            '@type': '%s#Project' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'},
            'Datasets': [{
                '@id': 1,
                '@type': '%s#Dataset' % OME_SCHEMA_URL,
                'Name': 'dataset_name_1',
                'Description': 'dataset_description_1',
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@id': 2,
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
            '@id': 1,
            '@type': '%s#Project' % OME_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'},
            'Datasets': [{
                '@id': 1,
                '@type': '%s#Dataset' % OME_SCHEMA_URL,
                'Name': 'dataset_name_1',
                'Description': 'dataset_description_1',
                'omero:details': {'@type': 'TBD#Details'},
                'Images': [{
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
                }, {
                    '@id': 2,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1,
                    'Name': 'image_name_2',
                    'omero:archived': False,
                    'Description': 'image_description_2',
                    'omero:partial': False,
                    'omero:series': 0,
                    'omero:format': {
                        '@id': 1,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                    'omero:details': {'@type': 'TBD#Details'}
                }]
            }, {
                '@id': 2,
                '@type': '%s#Dataset' % OME_SCHEMA_URL,
                'Name': 'dataset_name_2',
                'Description': 'dataset_description_2',
                'omero:details': {'@type': 'TBD#Details'},
                'Images': [{
                    '@id': 3,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1,
                    'Name': 'image_name_3',
                    'omero:archived': False,
                    'Description': 'image_description_3',
                    'omero:partial': False,
                    'omero:series': 0,
                    'omero:format': {
                        '@id': 1,
                        '@type': 'TBD#Format',
                        'value': 'PNG',
                        'omero:details': {'@type': 'TBD#Details'},
                    },
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 4,
                    '@type': '%s#Image' % OME_SCHEMA_URL,
                    'AcquisitionDate': 1,
                    'Name': 'image_name_4',
                    'omero:archived': False,
                    'Description': 'image_description_4',
                    'omero:partial': False,
                    'omero:series': 0,
                    'omero:format': {
                        '@id': 1,
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
            '@id': 4,
            '@type': '%s#Screen' % SPW_SCHEMA_URL,
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
            '@id': 4,
            '@type': '%s#Screen' % SPW_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'ProtocolDescription': 'the_protocol_description',
            'ProtocolIdentifier': 'the_protocol_identifier',
            'ReagentSetDescription': 'the_reagent_set_description',
            'ReagentSetIdentifier': 'the_reagent_set_identifier',
            'Type': 'the_type',
            'omero:details': {'@type': 'TBD#Details'},
            'Plates': [{
                '@id': 5,
                '@type': '%s#Plate' % SPW_SCHEMA_URL,
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
                    '@id': 7,
                    '@type': '%s#Well' % SPW_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_7',
                    'ExternalIdentifier': 'external_identifier_7',
                    'Type': 'the_type',
                    'Color': -16777216,
                    'omero:status': 'the_status',
                    'WellSamples': [{
                        '@id': 9,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 7,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_7',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_7',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 7,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_7',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_7',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 8,
                    '@type': '%s#Well' % SPW_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_8',
                    'ExternalIdentifier': 'external_identifier_8',
                    'Type': 'the_type',
                    'Color': -16777216,
                    'omero:status': 'the_status',
                    'WellSamples': [{
                        '@id': 9,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 8,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_8',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_8',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 8,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_8',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_8',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }],
                'omero:details': {'@type': 'TBD#Details'}
            }, {
                '@id': 6,
                '@type': '%s#Plate' % SPW_SCHEMA_URL,
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
                    '@id': 7,
                    '@type': '%s#Well' % SPW_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_7',
                    'ExternalIdentifier': 'external_identifier_7',
                    'Type': 'the_type',
                    'Color': -16777216,
                    'omero:status': 'the_status',
                    'WellSamples': [{
                        '@id': 9,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 7,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_7',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_7',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 7,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_7',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_7',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }, {
                    '@id': 8,
                    '@type': '%s#Well' % SPW_SCHEMA_URL,
                    'Column': 2,
                    'Row': 1,
                    'ExternalDescription': 'external_description_8',
                    'ExternalIdentifier': 'external_identifier_8',
                    'Type': 'the_type',
                    'Color': -16777216,
                    'omero:status': 'the_status',
                    'WellSamples': [{
                        '@id': 9,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 8,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_8',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_8',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }, {
                        '@id': 10,
                        '@type': '%s#WellSample' % SPW_SCHEMA_URL,
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
                        'Timepoint': 1,
                        'Image': {
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
                        },
                        'PlateAcquisition': {
                            '@id': 8,
                            '@type': '%s#PlateAcquisition' % SPW_SCHEMA_URL,
                            'Description': 'plateacquisition_description_8',
                            'EndTime': 2,
                            'MaximumFieldCount': 1,
                            'Name': 'plateacquisition_name_8',
                            'StartTime': 1,
                            'omero:details': {'@type': 'TBD#Details'}
                        },
                        'omero:details': {'@type': 'TBD#Details'}
                    }],
                    'omero:details': {'@type': 'TBD#Details'}
                }],
                'omero:details': {'@type': 'TBD#Details'}
            }]
        }
