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
from omero.model import DetailsI


class DetailsDecoder(Decoder):

    TYPE = 'TBD#Details'

    OMERO_CLASS = DetailsI

    def decode(self, data):
        v = DetailsI()
        owner = data.get('owner')
        if owner is not None:
            decoder = self.ctx.get_decoder(owner['@type'])
            v.owner = decoder.decode(owner)
        group = data.get('group')
        if group is not None:
            decoder = self.ctx.get_decoder(group['@type'])
            v.group = decoder.decode(group)
        permissions = data.get('permissions')
        if permissions is not None:
            decoder = self.ctx.get_decoder(permissions['@type'])
            v.permissions = decoder.decode(permissions)
        externalInfo = data.get('externalInfo')
        if externalInfo is not None:
            decoder = self.ctx.get_decoder(externalInfo['@type'])
            v.externalInfo = decoder.decode(externalInfo)
        return v


decoder = (DetailsDecoder.TYPE, DetailsDecoder)
