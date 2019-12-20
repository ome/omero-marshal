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

from omero_marshal import get_encoder, ROI_SCHEMA_URL, OME_SCHEMA_URL


class TestBaseEncoder(object):

    def test_base_encoder(self, roi):
        encoder = get_encoder(roi.__class__)
        v = encoder.encode(roi)
        assert v == {
            '@id': 1,
            '@type': '%s#ROI' % ROI_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {
                '@type': 'TBD#Details',
                'group': {
                    '@id': 1,
                    '@type': '%s#ExperimenterGroup' % OME_SCHEMA_URL,
                    'Description': 'the_description',
                    'Name': 'the_name',
                    'omero:details': {'@type': 'TBD#Details'}
                },
                'owner': {
                    '@id': 1,
                    '@type': '%s#Experimenter' % OME_SCHEMA_URL,
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
                    'perm': 'rwrwrw',
                    'isGroupAnnotate': True,
                    'isGroupRead': True,
                    'isGroupWrite': True,
                    'isUserRead': True,
                    'isUserWrite': True,
                    'isWorldRead': True,
                    'isWorldWrite': True
                },
                'externalInfo': {
                    '@type': 'TBD#ExternalInfo',
                    'EntityId': 123,
                    'EntityType': 'test',
                    'Lsid': 'ABCDEF',
                    'Uuid': 'f90a1fd5-275c-4d14-82b3-87b5ef0f07de',
                    'omero:details': {
                        '@type': 'TBD#Details'
                    },
                },
            }
        }

    def test_base_encoder_unloaded_details(self, roi):
        roi.unloadDetails()
        encoder = get_encoder(roi.__class__)
        v = encoder.encode(roi)
        assert v == {
            '@id': 1,
            '@type': '%s#ROI' % ROI_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description'
        }

    def test_base_encoder_with_unloaded_details_children(
            self, roi_with_unloaded_details_children):
        encoder = get_encoder(roi_with_unloaded_details_children.__class__)
        v = encoder.encode(roi_with_unloaded_details_children)
        assert v == {
            '@id': 1,
            '@type': '%s#ROI' % ROI_SCHEMA_URL,
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {
                '@type': 'TBD#Details',
                'owner': {
                    '@id': 1,
                    '@type': '%s#Experimenter' % OME_SCHEMA_URL
                },
                'group': {
                    '@id': 1,
                    '@type': '%s#ExperimenterGroup' % OME_SCHEMA_URL
                },
                'permissions': {
                    '@type': 'TBD#Permissions',
                    'canAnnotate': True,
                    'canDelete': True,
                    'canEdit': True,
                    'canLink': True,
                    'perm': 'rwrwrw',
                    'isGroupAnnotate': True,
                    'isGroupRead': True,
                    'isGroupWrite': True,
                    'isUserRead': True,
                    'isUserWrite': True,
                    'isWorldRead': True,
                    'isWorldWrite': True
                },
                'externalInfo': {
                    '@type': 'TBD#ExternalInfo',
                    'EntityId': 123,
                    'EntityType': 'test',
                    'Lsid': 'ABCDEF',
                    'Uuid': 'f90a1fd5-275c-4d14-82b3-87b5ef0f07de',
                    'omero:details': {
                        '@type': 'TBD#Details'
                    },
                },
            }
        }


class TestDetailsEncoder(object):

    def experimenter_json(self):
        return {
            '@id': 1,
            '@type': '%s#Experimenter' % OME_SCHEMA_URL,
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
            '@id': 1,
            '@type': '%s#ExperimenterGroup' % OME_SCHEMA_URL,
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
            'canLink': True,
            'isGroupAnnotate': True,
            'isGroupRead': True,
            'isGroupWrite': True,
            'isUserRead': True,
            'isUserWrite': True,
            'isWorldRead': True,
            'isWorldWrite': True
        }

    def test_permissions_encoder(self, permissions):
        encoder = get_encoder(permissions.__class__)
        v = encoder.encode(permissions)
        assert v == self.permissions_json()

    def externalInfo_json(self):
        return {
            '@type': 'TBD#ExternalInfo',
            'EntityId': 123,
            'EntityType': 'test',
            'Lsid': 'ABCDEF',
            'Uuid': 'f90a1fd5-275c-4d14-82b3-87b5ef0f07de',
            'omero:details': {
                '@type': 'TBD#Details'
            },
        }

    def test_externalInfo_encoder(self, externalInfo):
        encoder = get_encoder(externalInfo.__class__)
        v = encoder.encode(externalInfo)
        assert v == self.externalInfo_json()

    def test_details_encoder(self, details):
        encoder = get_encoder(details.__class__)
        v = encoder.encode(details)
        assert v == {
            '@type': 'TBD#Details',
            'permissions': self.permissions_json(),
            'owner': self.experimenter_json(),
            'group': self.experimenter_group_json(),
            'externalInfo': self.externalInfo_json(),
        }
