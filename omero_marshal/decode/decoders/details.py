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
from omero.model import Details


class DetailsDecoder(Decoder):

    TYPE = 'TBD#Details'

    OMERO_CLASS = Details

    def decode(self, data):
        v = Details()
        decoder = self.ctx.get_decoder(data['owner']['@type'])
        v.owner = decoder.decode(data['owner'])
        decoder = self.ctx.get_decoder(data['group']['@type'])
        v.group = decoder.decode(data['group'])
        decoder = self.ctx.get_decoder(data['details']['@type'])
        v.details = decoder.decode(data['details'])
        return v

decoder = (DetailsDecoder.TYPE, DetailsDecoder)
