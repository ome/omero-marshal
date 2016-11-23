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
from .. import Decoder
from omero.model import PixelsI


class Pixels201501Decoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Pixels'

    OMERO_CLASS = PixelsI

    def decode(self, data):
        v = super(Pixels201501Decoder, self).decode(data)
        self.set_property(v, 'methodology', data.get('omero:methodology'))
        v.physicalSizeX = self.to_unit(data.get('PhysicalSizeX'))
        v.physicalSizeY = self.to_unit(data.get('PhysicalSizeY'))
        v.physicalSizeZ = self.to_unit(data.get('PhysicalSizeZ'))
        self.set_property(v, 'sha1', data.get('omero:sha1'))
        self.set_property(v, 'significantBits', data.get('SignificantBits'))
        self.set_property(v, 'sizeX', data.get('SizeX'))
        self.set_property(v, 'sizeY', data.get('SizeY'))
        self.set_property(v, 'sizeZ', data.get('SizeZ'))
        self.set_property(v, 'sizeC', data.get('SizeC'))
        self.set_property(v, 'sizeT', data.get('SizeT'))
        v.timeIncrement = self.to_unit(data.get('TimeIncrement'))
        self.set_property(v, 'waveIncrement', data.get('omero:waveIncrement'))
        self.set_property(v, 'waveStart', data.get('omero:waveStart'))
        dimension_order = data.get('DimensionOrder')
        if dimension_order is not None:
            dimension_order_decoder = \
                self.ctx.get_decoder(dimension_order['@type'])
            v.dimensionOrder = dimension_order_decoder.decode(dimension_order)
        pixels_type = data.get('Type')
        if pixels_type is not None:
            pixels_type_decoder = \
                self.ctx.get_decoder(pixels_type['@type'])
            v.pixelsType = pixels_type_decoder.decode(pixels_type)
        channels = data.get('Channels', list())
        for channel in channels:
            channel_decoder = self.ctx.get_decoder(channel['@type'])
            v.addChannel(channel_decoder.decode(channel))
        return v


class Pixels201606Decoder(Pixels201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Pixels'


if SCHEMA_VERSION == '2015-01':
    decoder = (Pixels201501Decoder.TYPE, Pixels201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Pixels201606Decoder.TYPE, Pixels201606Decoder)
PixelsDecoder = decoder[1]
