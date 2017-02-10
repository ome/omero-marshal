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

    def set_property(self, target, prop, value):
        field_info = getattr(target._field_info, prop)
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        setattr(
            target,
            prop,
            field_info.wrapper(
                value
            ) if value is not None else None
        )

    def decode(self, data):
        o = self.OMERO_CLASS(data.get('@id'))
        details = data.get('omero:details')
        if details is not None:
            decoder = self.ctx.get_decoder(details['@type'])
            o._details = decoder.decode(details)
        return o

    @classmethod
    def int_to_rgba(cls, rgba_int):
        """Converts a color Integer into r, g, b, a tuple."""
        if rgba_int is None:
            return None, None, None, None
        alpha = rgba_int % 256
        blue = rgba_int / 256 % 256
        green = rgba_int / 256 / 256 % 256
        red = rgba_int / 256 / 256 / 256 % 256
        return (red, green, blue, alpha)
