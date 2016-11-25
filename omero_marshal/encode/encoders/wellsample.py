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
from .. import Encoder
from omero.model import WellSampleI


class WellSample201501Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#WellSample'

    def encode(self, obj):
        v = super(WellSample201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'PositionX', obj.posX)
        self.set_if_not_none(v, 'PositionY', obj.posY)
        self.set_if_not_none(v, 'Timepoint', obj.timepoint)
        if obj.image is not None and obj.image.isLoaded():
            image_encoder = self.ctx.get_encoder(obj.image.__class__)
            v['Image'] = image_encoder.encode(obj.image)
        return v


class WellSample201606Encoder(WellSample201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#WellSample'


if SCHEMA_VERSION == '2015-01':
    encoder = (WellSampleI, WellSample201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (WellSampleI, WellSample201606Encoder)
WellSampleEncoder = encoder[1]
