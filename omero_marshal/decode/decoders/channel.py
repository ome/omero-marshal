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
from .annotation import AnnotatableDecoder
from omero.model import ChannelI, LogicalChannelI


class Channel201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Channel'

    OMERO_CLASS = ChannelI

    def decode(self, data):
        v = super(Channel201501Decoder, self).decode(data)
        color = data.get('Color')
        red, green, blue, alpha = self.int_to_rgba(color)
        self.set_property(v, 'red', red)
        self.set_property(v, 'green', green)
        self.set_property(v, 'blue', blue)
        self.set_property(v, 'alpha', alpha)
        self.set_property(v, 'lookupTable', data.get('omero:lookupTable'))

        logical_channel = LogicalChannelI(data.get('omero:LogicalChannelId'))
        logical_channel.emissionWave = \
            self.to_unit(data.get('EmissionWavelength'))
        logical_channel.excitationWave = \
            self.to_unit(data.get('ExcitationWavelength'))
        self.set_property(logical_channel, 'fluor', data.get('Fluor'))
        self.set_property(logical_channel, 'name', data.get('Name'))
        self.set_property(logical_channel, 'ndFilter', data.get('NDFilter'))
        logical_channel.pinHoleSize = self.to_unit(data.get('PinholeSize'))
        self.set_property(
            logical_channel, 'pockelCellSetting', data.get('PockelCellSetting')
        )
        self.set_property(
            logical_channel, 'samplesPerPixel', data.get('SamplesPerPixel')
        )
        contrast_method = data.get('ContrastMethod')
        if contrast_method is not None:
            contrast_method_decoder = self.ctx.get_decoder(
                contrast_method['@type']
            )
            logical_channel.contrastMethod = contrast_method_decoder.decode(
                contrast_method
            )
        illumination = data.get('Illumination')
        if illumination is not None:
            illumination_decoder = self.ctx.get_decoder(
                illumination['@type']
            )
            logical_channel.illumination = illumination_decoder.decode(
                illumination
            )
        acquisition_mode = data.get('AcquisitionMode')
        if acquisition_mode is not None:
            acquisition_mode_decoder = self.ctx.get_decoder(
                acquisition_mode['@type']
            )
            logical_channel.mode = acquisition_mode_decoder.decode(
                acquisition_mode
            )
        photometric_interpretation = \
            data.get('omero:photometricInterpretation')
        if photometric_interpretation is not None:
            photometric_interpretation_decoder = self.ctx.get_decoder(
                photometric_interpretation['@type']
            )
            logical_channel.photometricInterpretation = \
                photometric_interpretation_decoder.decode(
                    photometric_interpretation
                )
        v.logicalChannel = logical_channel

        return v


class Channel201606Decoder(Channel201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Channel'


if SCHEMA_VERSION == '2015-01':
    decoder = (Channel201501Decoder.TYPE, Channel201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Channel201606Decoder.TYPE, Channel201606Decoder)
PixelsDecoder = decoder[1]
