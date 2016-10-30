#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from ... import SCHEMA_VERSION
from .. import Encoder
from omero.model import PixelsI


class Pixels201501Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Pixels'

    def encode(self, obj):
        v = super(Pixels201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'omero:methodology', obj.methodology)
        self.set_if_not_none(v, 'PhysicalSizeX', obj.physicalSizeX)
        self.set_if_not_none(v, 'PhysicalSizeY', obj.physicalSizeY)
        self.set_if_not_none(v, 'PhysicalSizeZ', obj.physicalSizeZ)
        self.set_if_not_none(v, 'omero:sha1', obj.sha1)
        self.set_if_not_none(v, 'SignificantBits', obj.significantBits)
        self.set_if_not_none(v, 'SizeX', obj.sizeX)
        self.set_if_not_none(v, 'SizeY', obj.sizeY)
        self.set_if_not_none(v, 'SizeZ', obj.sizeZ)
        self.set_if_not_none(v, 'SizeC', obj.sizeC)
        self.set_if_not_none(v, 'SizeT', obj.sizeT)
        self.set_if_not_none(v, 'TimeIncrement', obj.timeIncrement)
        self.set_if_not_none(v, 'omero:waveIncrement', obj.waveIncrement)
        self.set_if_not_none(v, 'omero:waveStart', obj.waveStart)
        if obj.dimensionOrder.isLoaded():
            encoder = self.ctx.get_encoder(obj.dimensionOrder.__class__)
            v['DimensionOrder'] = encoder.encode(obj.dimensionOrder)['value']
        if obj.pixelsType.isLoaded():
            encoder = self.ctx.get_encoder(obj.pixelsType.__class__)
            v['Type'] = encoder.encode(obj.pixelsType)['value']
        return v


class Pixels201606Encoder(Pixels201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Pixels'


if SCHEMA_VERSION == '2015-01':
    encoder = (PixelsI, Pixels201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PixelsI, Pixels201606Encoder)
PixelsEncoder = encoder[1]
