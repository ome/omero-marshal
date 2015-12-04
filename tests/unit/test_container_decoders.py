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
