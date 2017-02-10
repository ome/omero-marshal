#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from ... import SCHEMA_VERSION
from .. import Decoder
from omero.model import WellSampleI


class WellSample201501Decoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#WellSample'

    OMERO_CLASS = WellSampleI

    def decode(self, data):
        v = super(WellSample201501Decoder, self).decode(data)
        v.posX = self.to_unit(data.get('PositionX'))
        v.posY = self.to_unit(data.get('PositionY'))
        self.set_property(v, 'timepoint', data.get('Timepoint'))
        image = data.get('Image')
        if image is not None:
            image_decoder = self.ctx.get_decoder(image['@type'])
            v.image = image_decoder.decode(image)
        plateacquisition = data.get('PlateAcquisition')
        if plateacquisition is not None:
            plateacq_decoder = self.ctx.get_decoder(plateacquisition['@type'])
            v.plateAcquisition = plateacq_decoder.decode(plateacquisition)
        return v


class WellSample201606Decoder(WellSample201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#WellSample'


if SCHEMA_VERSION == '2015-01':
    decoder = (WellSample201501Decoder.TYPE, WellSample201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (WellSample201606Decoder.TYPE, WellSample201606Decoder)
WellSampleDecoder = decoder[1]
