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
        print data
        v = DetailsI()
        decoder = self.ctx.get_decoder(data['owner']['@type'])
        v.owner = decoder.decode(data['owner'])
        decoder = self.ctx.get_decoder(data['group']['@type'])
        v.group = decoder.decode(data['group'])
        decoder = self.ctx.get_decoder(data['permissions']['@type'])
        v.permissions = decoder.decode(data['permissions'])
        return v

decoder = (DetailsDecoder.TYPE, DetailsDecoder)
