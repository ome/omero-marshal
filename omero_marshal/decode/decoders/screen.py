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
from omero.model import ScreenI


class Screen201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#Screen'

    OMERO_CLASS = ScreenI

    def decode(self, data):
        v = super(Screen201501Decoder, self).decode(data)
        self.set_property(v, 'name', data.get('Name'))
        self.set_property(v, 'description', data.get('Description'))
        self.set_property(v, 'protocolDescription',
                          data.get('ProtocolDescription'))
        self.set_property(v, 'protocolIdentifier',
                          data.get('ProtocolIdentifier'))
        self.set_property(v, 'reagentSetDescription',
                          data.get('ReagentSetDescription'))
        self.set_property(v, 'reagentSetIdentifier',
                          data.get('ReagentSetIdentifier'))
        self.set_property(v, 'type', data.get('Type'))
        for plate in data.get('Plates', list()):
            plate_decoder = self.ctx.get_decoder(plate['@type'])
            v.linkPlate(plate_decoder.decode(plate))
        return v


class Screen201606Decoder(Screen201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Screen'


if SCHEMA_VERSION == '2015-01':
    decoder = (Screen201501Decoder.TYPE, Screen201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Screen201606Decoder.TYPE, Screen201606Decoder)
ScreenDecoder = decoder[1]
