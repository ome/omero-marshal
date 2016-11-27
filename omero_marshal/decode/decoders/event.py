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

from .. import Decoder
from omero.model import EventI


class EventDecoder(Decoder):

    TYPE = 'TBD#Event'

    OMERO_CLASS = EventI

    def decode(self, data):
        v = super(EventDecoder, self).decode(data)
        self.set_property(v, 'status', data.get('status'))
        self.set_property(v, 'time', data.get('time'))

        experimenter = data.get('experimenter')
        if experimenter is not None:
            decoder = self.ctx.get_decoder(experimenter['@type'])
            v.experimenter = decoder.decode(experimenter)
        experimenterGroup = data.get('experimenterGroup')
        if experimenterGroup is not None:
            decoder = self.ctx.get_decoder(experimenterGroup['@type'])
            v.experimenterGroup = decoder.decode(experimenterGroup)
        _type = data.get('type')
        if _type is not None:
            decoder = self.ctx.get_decoder(_type['@type'])
            v.type = decoder.decode(_type)
        return v

decoder = (EventDecoder.TYPE, EventDecoder)
