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
from omero.model import WellI


class Well201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Well'

    def encode(self, obj):
        v = super(Well201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Column', obj.column)
        self.set_if_not_none(v, 'Row', obj.row)
        self.set_if_not_none(v, 'ExternalDescription', obj.externalDescription)
        self.set_if_not_none(v, 'ExternalIdentifier', obj.externalIdentifier)
        self.set_if_not_none(v, 'Type', obj.type)
        # FIXME: Color conversion required (uses integer encoded Color field)
        self.set_if_not_none(v, 'Alpha', obj.alpha)
        self.set_if_not_none(v, 'Red', obj.red)
        self.set_if_not_none(v, 'Green', obj.green)
        self.set_if_not_none(v, 'Blue', obj.blue)
        self.set_if_not_none(v, 'omero:status', obj.status)

        if obj.isWellSamplesLoaded() and obj.sizeOfWellSamples() > 0:
            wellsamples = list()
            for wellsample in obj.copyWellSamples():
                wellsample_encoder = self.ctx.get_encoder(wellsample.__class__)
                wellsamples.append(
                    wellsample_encoder.encode(wellsample)
                )
            v['WellSamples'] = wellsamples
        return v


class Well201606Encoder(Well201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Well'


if SCHEMA_VERSION == '2015-01':
    encoder = (WellI, Well201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (WellI, Well201606Encoder)
WellEncoder = encoder[1]
