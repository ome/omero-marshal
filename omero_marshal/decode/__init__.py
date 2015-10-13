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
        unit = v['@type'][v['@type'].rfind('#') + 1:]
        unit = getattr(omero.model, unit)
        unit_unit = v['Unit']['@type'][v['Unit']['@type'].rfind('#') + 1:]
        unit_unit = getattr(omero.model.enums, unit_unit)
        return unit(
            float(v['Value']),
            getattr(unit_unit, v['Unit']['Name'])
        )

    def to_rtype(self, v):
        if isinstance(v, unicode):
            v = v.encode('utf-8')
        return rtype(v)

    def decode(self, data):
        return self.OMERO_CLASS(data.get('@id'))
