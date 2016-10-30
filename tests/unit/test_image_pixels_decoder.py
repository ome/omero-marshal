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

    def test_image_decoder(self, image):
        encoder = get_encoder(image.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(image)
        v = decoder.decode(v)
        assert v.id.val == 1L
        assert v.acquisitionDate.val == 1L
        assert v.archived.val == False
        assert v.description.val == 'image_description_1'
        assert v.name.val == 'image_name_1'
        assert v.partial.val == False
        assert v.format.id.val == 1L
        assert v.format.value.val == 'PNG'

    def test_image_pixels_decoder(self, image_pixels):
        encoder = get_encoder(image_pixels.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(image_pixels)
        v = decoder.decode(v)
        assert v.id.val == 1L
        assert v.acquisitionDate.val == 1L
        assert v.archived.val == False
        assert v.description.val == 'image_description_1'
        assert v.name.val == 'image_name_1'
        assert v.partial.val == False
        assert v.format.id.val == 1L
        assert v.format.value.val == 'PNG'

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
