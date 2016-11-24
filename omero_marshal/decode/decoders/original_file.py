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
from omero.model import OriginalFileI


class OriginalFileDecoder(Decoder):

    TYPE = 'TBD#OriginalFile'

    OMERO_CLASS = OriginalFileI

    def decode(self, data):
        v = super(OriginalFileDecoder, self).decode(data)
        self.set_property(v, 'path', data.get('path'))
        self.set_property(v, 'size', data.get('size'))
        self.set_property(v, 'atime', data.get('atime'))
        self.set_property(v, 'mtime', data.get('mtime'))
        self.set_property(v, 'ctime', data.get('ctime'))
        self.set_property(v, 'hash', data.get('hash'))
        self.set_property(v, 'mimetype', data.get('mimetype'))
        self.set_property(v, 'name', data.get('name'))

        hasher = data.get('hasher')
        if hasher is not None:
            checksum_algorithm_decoder = self.ctx.get_decoder(hasher['@type'])
            v.hasher = checksum_algorithm_decoder.decode(hasher)
        return v


decoder = (OriginalFileDecoder.TYPE, OriginalFileDecoder)
