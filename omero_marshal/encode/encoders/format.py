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
from omero.model import FormatI


class FormatEncoder(Encoder):

    TYPE = 'TBD#Format'

    def encode(self, obj):
        v = super(FormatEncoder, self).encode(obj)
        if not obj.isLoaded():
            return v
        self.set_if_not_none(v, 'value', obj.value)
        return v

encoder = (FormatI, FormatEncoder)
