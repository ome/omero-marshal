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
        dimension_order = obj.dimensionOrder
        if dimension_order is not None and dimension_order.isLoaded():
            dimension_order_encoder = \
                self.ctx.get_encoder(dimension_order.__class__)
            v['DimensionOrder'] = \
                dimension_order_encoder.encode(dimension_order)
        pixels_type = obj.pixelsType
        if pixels_type is not None and pixels_type.isLoaded():
            pixels_type_encoder = \
                self.ctx.get_encoder(pixels_type.__class__)
            v['Type'] = pixels_type_encoder.encode(pixels_type)
        if obj.isChannelsLoaded() and obj.sizeOfChannels() > 0:
            channels = list()
            for channel in obj.copyChannels():
                channel_encoder = self.ctx.get_encoder(channel.__class__)
                channels.append(channel_encoder.encode(channel))
            v['Channels'] = channels
        return v


class Pixels201606Encoder(Pixels201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Pixels'


if SCHEMA_VERSION == '2015-01':
    encoder = (PixelsI, Pixels201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PixelsI, Pixels201606Encoder)
PixelsEncoder = encoder[1]
