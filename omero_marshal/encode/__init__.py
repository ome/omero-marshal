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

# Needed to avoid import errors when this is the first import
import omero.all  # noqa
from omero import RType
from omero_model_UnitBase import UnitBase
from omero.rtypes import unwrap


BASE_CONTEXT = "http://www.openmicroscopy.org/Schemas/OME/2016-06#"
OMERO_CONTEXT = "http://www.openmicroscopy.org/Schemas/OMERO/2016-06#"


class Encoder(object):

    TYPE = ''

    def __init__(self, ctx):
        self.ctx = ctx

    def set_if_not_none(self, v, key, value):
        if value is None:
            return
        if isinstance(value, RType):
            v[key] = value.getValue()
        elif isinstance(value, UnitBase):
            self.encode_unit(v, key, value)
        else:
            v[key] = value

    def encode_unit(self, v, key, value):
        k = value.__class__.__name__
        if k in ("LengthI", "TimeI"):
            v[key] = {
                '@type': 'omero:%s' % k,
                'Unit': value.getUnit().name,
                'Symbol': value.getSymbol(),
                'Value': value.getValue()
            }
        else:
            raise Exception("unhandled unit: %s" % k)

    def encode(self, obj, include_context=None):

        if self.TYPE.startswith(BASE_CONTEXT):
            v = {'@type': self.TYPE.split('#')[-1]}
        elif self.TYPE.startswith(OMERO_CONTEXT):
            v = {'@type': "omero:" + self.TYPE.split('#')[-1]}
        else:
            raise Exception("unknown prefix: %s" % self.TYPE)

        if include_context is None or include_context:
            v['@context'] = {
                "@base": BASE_CONTEXT,
                "omero": OMERO_CONTEXT,
            }

        if hasattr(obj, 'id'):
            obj_id = unwrap(obj.id)
            if obj_id is not None:
                v['@id'] = obj_id
        if hasattr(obj, 'details') and obj.details is not None:
            encoder = self.ctx.get_encoder(obj.details.__class__)
            v['omero:details'] = encoder.encode(obj.details, False)

        return v

    @classmethod
    def rgba_to_int(cls, red, green, blue, alpha):
        """
        Encodes the color as an Integer in RGBA encoding

        Returns None if any of red, green or blue are None.
        If alpha is None we use 255 by default.

        :return:    Integer
        :rtype:     int
        """
        red = unwrap(red)
        green = unwrap(green)
        blue = unwrap(blue)
        alpha = unwrap(alpha)
        if red is None or green is None or blue is None:
            return None
        if alpha is None:
            alpha = 255
        r = red << 24
        g = green << 16
        b = blue << 8
        a = alpha << 0
        rgba_int = r+g+b+a
        if (rgba_int > (2**31-1)):       # convert to signed 32-bit int
            rgba_int = rgba_int - 2**32
        return rgba_int
