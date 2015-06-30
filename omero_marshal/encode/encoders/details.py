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
from omero.model import DetailsI


class DetailsEncoder(Encoder):

    TYPE = 'TBD#Details'

    def encode(self, obj):
        v = super(DetailsEncoder, self).encode(obj)
        encoder = self.ctx.get_encoder(obj.owner.__class__)
        v['owner'] = encoder.encode(obj.owner)
        encoder = self.ctx.get_encoder(obj.group.__class__)
        v['group'] = encoder.encode(obj.group)
        encoder = self.ctx.get_encoder(obj.permissions.__class__)
        v['permissions'] = encoder.encode(obj.permissions)
        return v

encoder = (DetailsI, DetailsEncoder)
