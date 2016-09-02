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

from ... import SCHEMA_VERSION
from .annotation import AnnotatableDecoder
from omero.model import ProjectI


class Project201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Project'

    OMERO_CLASS = ProjectI

    def decode(self, data):
        v = super(Project201501Decoder, self).decode(data)
        self.set_property(v, 'name', data.get('Name'))
        self.set_property(v, 'description', data.get('Description'))
        for dataset in data.get('Datasets', list()):
            dataset_decoder = self.ctx.get_decoder(dataset['@type'])
            v.linkDataset(dataset_decoder.decode(dataset))
        return v


class Project201606Decoder(Project201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Project'


if SCHEMA_VERSION == '2015-01':
    decoder = (Project201501Decoder.TYPE, Project201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Project201606Decoder.TYPE, Project201606Decoder)
ProjectDecoder = decoder[1]
