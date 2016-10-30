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
from omero.model import ChannelI


class Channel201501Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Channel'

    def encode(self, obj):
        v = super(Channel201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Alpha', obj.alpha)
        self.set_if_not_none(v, 'Blue', obj.blue)
        self.set_if_not_none(v, 'Green', obj.green)
        self.set_if_not_none(v, 'Red', obj.red)
        self.set_if_not_none(v, 'omero:lookupTable', obj.lookupTable)
        logical_channel = obj.logicalChannel
        if logical_channel is not None and logical_channel.isLoaded():
            self.set_if_not_none(
                v, 'EmissionWavelength', logical_channel.emissionWave
            )
            self.set_if_not_none(
                v, 'ExcitationWavelength', logical_channel.excitationWave
            )
            self.set_if_not_none(v, 'Fluor', logical_channel.fluor)
            self.set_if_not_none(v, 'Name', logical_channel.name)
            self.set_if_not_none(v, 'NDFilter', logical_channel.ndFilter)
            self.set_if_not_none(v, 'PinholeSize', logical_channel.pinHoleSize)
            self.set_if_not_none(
                v, 'PockelCellSetting', logical_channel.pockelCellSetting
            )
            self.set_if_not_none(
                v, 'SamplesPerPixel', logical_channel.samplesPerPixel
            )
            contrast_method = logical_channel.contrastMethod
            if contrast_method is not None and contrast_method.isLoaded():
                contrast_method_encoder = \
                    self.ctx.get_encoder(contrast_method.__class__)
                v['ContrastMethod'] = \
                    contrast_method_encoder.encode(contrast_method)
            illumination = logical_channel.illumination
            if illumination is not None and illumination.isLoaded():
                illumination_encoder = \
                    self.ctx.get_encoder(illumination.__class__)
                v['Illumination'] = \
                    illumination_encoder.encode(illumination)
            acquisition_mode = logical_channel.mode
            if acquisition_mode is not None and acquisition_mode.isLoaded():
                acquisition_mode_encoder = \
                    self.ctx.get_encoder(acquisition_mode.__class__)
                v['AcquisitionMode'] = \
                    acquisition_mode_encoder.encode(acquisition_mode)
            photometric_interpretation = \
                logical_channel.photometricInterpretation
            if photometric_interpretation is not None \
                    and photometric_interpretation.isLoaded():
                photometric_interpretation_encoder = \
                    self.ctx.get_encoder(photometric_interpretation.__class__)
                v['photometricInterpretation'] = \
                    photometric_interpretation_encoder.encode(
                        photometric_interpretation
                    )
        return v

"""
    channel_1 = ChannelI(1L)
    channel_1.alpha = rint(255)
    channel_1.blue = rint(0)
    channel_1.green = rint(255)
    channel_1.red = rint(0)
    channel_1.lookupTable = rstring('rainbow')
    logical_channel_1 = LogicalChannelI(1L)
    logical_channel_1.emissionWave = LengthI(509.0, UnitsLength.NANOMETER)
    logical_channel_1.excitationWave = LengthI(488.0, UnitsLength.NANOMETER)
    logical_channel_1.fluor = rstring('GFP')
    logical_channel_1.name = rstring('GFP/488')
    logical_channel_1.ndFilter = rdouble(1.0)
    logical_channel_1.pinHoleSize = LengthI(1.0, UnitsLength.NANOMETER)
    logical_channel_1.pockelCellSetting = rint(0)
    logical_channel_1.samplesPerPixel = rint(2)
    logical_channel_1.contrastMethod = contrast_method
    logical_channel_1.illumination = illumination
    logical_channel_1.mode = acquisition_mode
    logical_channel_1.photometricInterpretation = photometric_interpretation
"""


class Channel201606Encoder(Channel201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Channel'


if SCHEMA_VERSION == '2015-01':
    encoder = (ChannelI, Channel201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (ChannelI, Channel201606Encoder)
ChannelEncoder = encoder[1]
