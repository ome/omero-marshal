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
from omero.model import RoiI


class Roi201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'

    def encode(self, obj):
        v = super(Roi201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        if obj.isShapesLoaded() and obj.sizeOfShapes() > 0:
            shapes = list()
            for shape in obj.copyShapes():
                shape_encoder = self.ctx.get_encoder(shape.__class__)
                shapes.append(shape_encoder.encode(shape))
            v['shapes'] = shapes
        return v


class Roi201606Encoder(Roi201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#ROI'


if SCHEMA_VERSION == '2015-01':
    encoder = (RoiI, Roi201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (RoiI, Roi201606Encoder)
RoiEncoder = encoder[1]
