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

import omero.model
import omero.model.enums

from omero.rtypes import rtype


class Decoder(object):

    TYPE = ''

    OMERO_CLASS = None

    def __init__(self, ctx):
        self.ctx = ctx

    def to_unit(self, v):
        if v is None:
            return None
        unit = v['@type'][v['@type'].rfind('#') + 1:]
        unit = getattr(omero.model, unit)
        return unit(
            float(v['Value']),
            v['Unit']
        )

    def to_rtype(self, v):
        if isinstance(v, unicode):
            v = v.encode('utf-8')
        return rtype(v)

    def decode(self, data):
        o = self.OMERO_CLASS(data.get('@id'))
        details = data.get('omero:details')
        if details is not None:
            decoder = self.ctx.get_decoder(details['@type'])
            o._details = decoder.decode(details)
        return o
