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

from .annotation import AnnotatableDecoder
from omero.model import ProjectI


class ProjectDecoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Project'

    OMERO_CLASS = ProjectI

    def decode(self, data):
        v = super(ProjectDecoder, self).decode(data)
        v.name = self.to_rtype(data.get('Name'))
        v.description = self.to_rtype(data.get('Description'))
        for dataset in data.get('Datasets', list()):
            dataset_decoder = self.ctx.get_decoder(dataset['@type'])
            v.linkDataset(dataset_decoder.decode(dataset))
        return v

decoder = (ProjectDecoder.TYPE, ProjectDecoder)
