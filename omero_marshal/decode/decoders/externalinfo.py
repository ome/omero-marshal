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
from omero.model import ExternalInfoI


class ExternalInfoDecoder(Decoder):

    TYPE = 'TBD#ExternalInfo'

    OMERO_CLASS = ExternalInfoI

    def decode(self, data):
        v = super(ExternalInfoDecoder, self).decode(data)
        v.entityId = self.to_rtype(data.get('EntityId'))
        v.entityType = self.to_rtype(data.get('EntityType'))
        v.lsid = self.to_rtype(data.get('Lsid'))
        v.uuid = self.to_rtype(data.get('Uuid'))
        return v

decoder = (ExternalInfoDecoder.TYPE, ExternalInfoDecoder)
