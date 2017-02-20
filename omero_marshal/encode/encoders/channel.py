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
from .annotation import AnnotatableEncoder
from omero.model import ChannelI


class Channel201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Channel'

    def encode(self, obj):
        v = super(Channel201501Encoder, self).encode(obj)
        color = self.rgba_to_int(obj.red, obj.green, obj.blue, obj.alpha)
        self.set_if_not_none(v, 'Color', color)
        self.set_if_not_none(v, 'omero:lookupTable', obj.lookupTable)
        logical_channel = obj.logicalChannel
        if logical_channel is not None and logical_channel.isLoaded():
            self.set_if_not_none(
                v, 'omero:LogicalChannelId', logical_channel.id
            )
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
                v['omero:photometricInterpretation'] = \
                    photometric_interpretation_encoder.encode(
                        photometric_interpretation
                    )
        return v


class Channel201606Encoder(Channel201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Channel'


if SCHEMA_VERSION == '2015-01':
    encoder = (ChannelI, Channel201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (ChannelI, Channel201606Encoder)
ChannelEncoder = encoder[1]
