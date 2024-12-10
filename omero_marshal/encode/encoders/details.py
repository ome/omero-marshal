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

    TYPE = 'http://www.openmicroscopy.org/Schemas/OMERO/2016-06#Details'

    def encode(self, obj, include_context=None):
        # Never include contexts on these objects
        v = super(DetailsEncoder, self).encode(obj, False)
        if obj.owner is not None:
            encoder = self.ctx.get_encoder(obj.owner.__class__)
            v['owner'] = encoder.encode(obj.owner, False)
        if obj.group is not None:
            encoder = self.ctx.get_encoder(obj.group.__class__)
            v['group'] = encoder.encode(obj.group, False)
        if obj.permissions is not None:
            encoder = self.ctx.get_encoder(obj.permissions.__class__)
            v['permissions'] = encoder.encode(obj.permissions, False)
        if obj.externalInfo is not None:
            encoder = self.ctx.get_encoder(obj.externalInfo.__class__)
            v['externalInfo'] = encoder.encode(obj.externalInfo, False)
        return v


encoder = (DetailsI, DetailsEncoder)
