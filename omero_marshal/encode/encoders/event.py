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

from .. import Encoder
from omero.model import EventI


class EventEncoder(Encoder):

    TYPE = 'TBD#Event'

    def encode(self, obj):
        v = super(EventEncoder, self).encode(obj)
        self.set_if_not_none(v, 'status', obj.status)
        self.set_if_not_none(v, 'time', obj.time)
        if obj.experimenter is not None:
            encoder = self.ctx.get_encoder(obj.experimenter.__class__)
            v['experimenter'] = encoder.encode(obj.experimenter)
        if obj.experimenterGroup is not None:
            encoder = self.ctx.get_encoder(obj.experimenterGroup.__class__)
            v['experimenterGroup'] = encoder.encode(obj.experimenterGroup)
        if obj.type is not None:
            encoder = self.ctx.get_encoder(obj.type.__class__)
            v['type'] = encoder.encode(obj.type)
        return v

encoder = (EventI, EventEncoder)
