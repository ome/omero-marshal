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
from .annotation import AnnotatableEncoder
from omero.model import ScreenI


class Screen201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#Screen'

    def encode(self, obj):
        v = super(Screen201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'ProtocolDescription', obj.protocolDescription)
        self.set_if_not_none(v, 'ProtocolIdentifier', obj.protocolIdentifier)
        self.set_if_not_none(v, 'ReagentSetDescription',
                             obj.reagentSetDescription)
        self.set_if_not_none(v, 'ReagentSetIdentifier',
                             obj.reagentSetIdentifier)
        self.set_if_not_none(v, 'Type', obj.type)
        if obj.isPlateLinksLoaded() and obj.sizeOfPlateLinks() > 0:
            plates = list()
            for plate_link in obj.copyPlateLinks():
                plate = plate_link.child
                plate_encoder = self.ctx.get_encoder(plate.__class__)
                plates.append(
                    plate_encoder.encode(plate)
                )
            v['Plates'] = plates
        return v


class Screen201606Encoder(Screen201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Screen'


if SCHEMA_VERSION == '2015-01':
    encoder = (ScreenI, Screen201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (ScreenI, Screen201606Encoder)
ScreenEncoder = encoder[1]
