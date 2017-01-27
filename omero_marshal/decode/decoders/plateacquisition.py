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
from .annotation import AnnotatableDecoder
from omero.model import PlateAcquisitionI


class PlateAcquisition201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#PlateAcquisition'

    OMERO_CLASS = PlateAcquisitionI

    def decode(self, data):
        v = super(PlateAcquisition201501Decoder, self).decode(data)
        self.set_property(v, 'name', data.get('Name'))
        self.set_property(v, 'description', data.get('Description'))
        self.set_property(
            v, 'maximumFieldCount', data.get('MaximumFieldCount')
        )
        self.set_property(v, 'startTime', data.get('StartTime'))
        self.set_property(v, 'endTime', data.get('EndTime'))
        return v


class PlateAcquisition201606Decoder(PlateAcquisition201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#PlateAcquisition'


if SCHEMA_VERSION == '2015-01':
    decoder = (PlateAcquisition201501Decoder.TYPE,
               PlateAcquisition201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (PlateAcquisition201606Decoder.TYPE,
               PlateAcquisition201606Decoder)
PlateAcquisitionDecoder = decoder[1]
