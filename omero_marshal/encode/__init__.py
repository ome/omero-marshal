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

from omero.rtypes import unwrap


class Encoder(object):

    TYPE = ''

    def set_if_not_none(self, v, key, value):
        if value is not None:
            v[key] = value.getValue()

    def encode(self, obj):
        obj_id = unwrap(obj.id)
        v = {'@type': self.TYPE}
        if obj_id is not None:
            v['@id'] = obj_id
        return v
