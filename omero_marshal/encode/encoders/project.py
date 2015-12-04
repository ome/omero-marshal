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

from .annotation import AnnotatableEncoder
from omero.model import ProjectI


class ProjectEncoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Project'

    def encode(self, obj):
        v = super(ProjectEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        if obj.isDatasetLinksLoaded() and obj.sizeOfDatasetLinks() > 0:
            datasets = list()
            for dataset_link in obj.copyDatasetLinks():
                dataset = dataset_link.child
                dataset_encoder = self.ctx.get_encoder(dataset.__class__)
                datasets.append(
                    dataset_encoder.encode(dataset)
                )
            v['Datasets'] = datasets
        return v

encoder = (ProjectI, ProjectEncoder)
