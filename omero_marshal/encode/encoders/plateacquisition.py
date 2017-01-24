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
from .annotation import AnnotatableEncoder
from omero.model import PlateAcquisitionI


class PlateAcquisition201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#PlateAcquisition'

    def encode(self, obj):
        v = super(PlateAcquisition201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'MaximumFieldCount', obj.maximumFieldCount)
        self.set_if_not_none(v, 'StartTime', obj.startTime)
        self.set_if_not_none(v, 'EndTime', obj.endTime)
        return v


class PlateAcquisition201606Encoder(PlateAcquisition201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#PlateAcquisition'


if SCHEMA_VERSION == '2015-01':
    encoder = (PlateAcquisitionI, PlateAcquisition201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PlateAcquisitionI, PlateAcquisition201606Encoder)
PlateAcquisitionEncoder = encoder[1]
