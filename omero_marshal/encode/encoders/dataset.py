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
from .annotation import AnnotatableEncoder
from omero.model import DatasetI


class Dataset201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Dataset'

    def encode(self, obj):
        v = super(Dataset201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        if obj.isImageLinksLoaded() and obj.sizeOfImageLinks() > 0:
            images = list()
            for image_link in obj.copyImageLinks():
                image = image_link.child
                image_encoder = self.ctx.get_encoder(image.__class__)
                images.append(
                    image_encoder.encode(image)
                )
            v['Images'] = images
        return v


class Dataset201606Encoder(Dataset201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Dataset'


if SCHEMA_VERSION == '2015-01':
    encoder = (DatasetI, Dataset201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (DatasetI, Dataset201606Encoder)
DatasetEncoder = encoder[1]
