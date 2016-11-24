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
from omero.model import OriginalFileI


class OriginalFileEncoder(Encoder):

    TYPE = 'TBD#OriginalFile'

    def encode(self, obj):
        v = super(OriginalFileEncoder, self).encode(obj)
        self.set_if_not_none(v, 'path', obj.path)
        self.set_if_not_none(v, 'size', obj.size)
        self.set_if_not_none(v, 'atime', obj.atime)
        self.set_if_not_none(v, 'mtime', obj.mtime)
        self.set_if_not_none(v, 'ctime', obj.ctime)
        self.set_if_not_none(v, 'hash', obj.hash)
        self.set_if_not_none(v, 'mimetype', obj.mimetype)
        self.set_if_not_none(v, 'name', obj.name)
        if obj.hasher is not None and obj.hasher.isLoaded():
            checksum_algorithm_encoder = \
                self.ctx.get_encoder(obj.hasher.__class__)
            v['hasher'] = \
                checksum_algorithm_encoder.encode(obj.hasher)
        return v


encoder = (OriginalFileI, OriginalFileEncoder)
