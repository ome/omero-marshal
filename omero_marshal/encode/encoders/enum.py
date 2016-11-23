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


class EnumEncoder(Encoder):

    def __init__(self, ctx):
        super(EnumEncoder, self).__init__(ctx)

    def encode(self, obj):
        v = super(EnumEncoder, self).encode(obj)
        self.set_if_not_none(v, 'value', obj.value)
        return v
