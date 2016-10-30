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

from omero_marshal import get_encoder, get_decoder
from omero.model.enums import UnitsLength, UnitsTime


class TestImagePixelsDecoder(object):

    def assert_image(self, v):
        assert v.id.val == 1L
        assert v.acquisitionDate.val == 1L
        assert v.archived.val is False
        assert v.description.val == 'image_description_1'
        assert v.name.val == 'image_name_1'
        assert v.partial.val is False
        assert v.series.val == 0L
        assert v.format.id.val == 1L
        assert v.format.value.val == 'PNG'

    def test_image_decoder(self, image):
        encoder = get_encoder(image.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(image)
        v = decoder.decode(v)
        self.assert_image(v)

    def test_image_pixels_decoder(self, image_pixels):
        encoder = get_encoder(image_pixels.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(image_pixels)
        v = decoder.decode(v)
        self.assert_image(v)

        pixels = v.getPrimaryPixels()
        assert pixels.id.val == 1L
        assert pixels.methodology.val == 'methodology'
        assert pixels.physicalSizeX.getUnit() == UnitsLength.MICROMETER
        assert pixels.physicalSizeX.getValue() == 1.0
        assert pixels.physicalSizeY.getUnit() == UnitsLength.MICROMETER
        assert pixels.physicalSizeY.getValue() == 2.0
        assert pixels.physicalSizeZ.getUnit() == UnitsLength.MICROMETER
        assert pixels.physicalSizeZ.getValue() == 3.0
        assert pixels.sha1.val == '61ee8b5601a84d5154387578466c8998848ba089'
        assert pixels.significantBits.val == 16
        assert pixels.sizeX.val == 1
        assert pixels.sizeY.val == 2
        assert pixels.sizeZ.val == 3
        assert pixels.sizeC.val == 4
        assert pixels.sizeT.val == 5
        assert pixels.timeIncrement.getUnit() == UnitsTime.MILLISECOND
        assert pixels.timeIncrement.getValue() == 1.0
        assert pixels.waveIncrement.val == 2.0
        assert pixels.waveStart.val == 1
        assert pixels.dimensionOrder.id.val == 1L
        assert pixels.dimensionOrder.value.val == 'XYZCT'
        assert pixels.pixelsType.id.val == 1L
        assert pixels.pixelsType.value.val == 'bit'

        channel_1, channel_2 = pixels.copyChannels()
        assert channel_1.id.val == 1L
        assert channel_1.alpha.val == 255
        assert channel_1.blue.val == 0
        assert channel_1.green.val == 255
        assert channel_1.red.val == 0
        assert channel_1.lookupTable.val == 'rainbow'
        logical_channel_1 = channel_1.logicalChannel
        assert logical_channel_1.id.val == 1L
        assert logical_channel_1.emissionWave.getUnit() \
            == UnitsLength.NANOMETER
        assert logical_channel_1.emissionWave.getValue() == 509.0
        assert logical_channel_1.excitationWave.getUnit() \
            == UnitsLength.NANOMETER
        assert logical_channel_1.excitationWave.getValue() == 488.0
        assert logical_channel_1.fluor.val == 'GFP'
        assert logical_channel_1.name.val == 'GFP/488'
        assert logical_channel_1.ndFilter.val == 1.0
        assert logical_channel_1.pinHoleSize.getUnit() == UnitsLength.NANOMETER
        assert logical_channel_1.pinHoleSize.getValue() == 1.0
        assert logical_channel_1.pockelCellSetting.val == 0
        assert logical_channel_1.samplesPerPixel.val == 2
        assert logical_channel_1.contrastMethod.value.val == 'Fluorescence'
        assert logical_channel_1.illumination.value.val == 'Transmitted'
        assert logical_channel_1.mode.value.val == 'WideField'
        assert logical_channel_1.photometricInterpretation.value.val == 'RGB'
