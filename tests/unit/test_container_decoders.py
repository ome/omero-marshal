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

from omero_marshal import get_encoder, get_decoder


class TestProjectDecoder(object):

    def assert_project(self, project):
        assert project.name.val == 'the_name'
        assert project.description.val == 'the_description'

    def test_project_decoder(self, project):
        encoder = get_encoder(project.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project)
        v = decoder.decode(v)
        self.assert_project(v)
        assert v.sizeOfDatasetLinks() == 0

    def test_project_with_datasets_decoder(self, project_with_datasets):
        encoder = get_encoder(project_with_datasets.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project_with_datasets)
        v = decoder.decode(v)
        assert v.id.val == 1L
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfDatasetLinks() == 2
        dataset_1, dataset_2 = v.linkedDatasetList()
        assert dataset_1.id.val == 1L
        assert dataset_1.name.val == 'dataset_name_1'
        assert dataset_1.description.val == 'dataset_description_1'
        assert dataset_2.id.val == 2L
        assert dataset_2.name.val == 'dataset_name_2'
        assert dataset_2.description.val == 'dataset_description_2'


class TestScreenDecoder(object):

    def assert_screen(self, screen):
        assert screen.name.val == 'the_name'
        assert screen.description.val == 'the_description'

    def test_screen_decoder(self, screen):
        encoder = get_encoder(screen.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(screen)
        v = decoder.decode(v)
        self.assert_screen(v)
        assert v.sizeOfPlateLinks() == 0

    def test_screen_with_plates_decoder(self, screen_with_plates):
        encoder = get_encoder(screen_with_plates.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(screen_with_plates)
        v = decoder.decode(v)
        assert v.id.val == 4L
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfPlateLinks() == 2
        plate_1, plate_2 = v.linkedPlateList()
        assert plate_1.id.val == 5L
        assert plate_1.name.val == 'plate_name_5'
        assert plate_1.description.val == 'plate_description_5'
        assert plate_2.id.val == 6L
        assert plate_2.name.val == 'plate_name_6'
        assert plate_2.description.val == 'plate_description_6'
