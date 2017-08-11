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
from .shape import ShapeDecoder
from omero.model import MaskI


class Mask201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Mask'

    OMERO_CLASS = MaskI

    def decode(self, data):
        v = super(Mask201501Decoder, self).decode(data)
        self.set_property(v, 'x', data.get('X'))
        self.set_property(v, 'y', data.get('Y'))
        self.set_property(v, 'width', data.get('Width'))
        self.set_property(v, 'height', data.get('Height'))
        return v


class Mask201606Decoder(Mask201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Mask'


if SCHEMA_VERSION == '2015-01':
    decoder = (Mask201501Decoder.TYPE, Mask201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Mask201606Decoder.TYPE, Mask201606Decoder)
MaskDecoder = decoder[1]
