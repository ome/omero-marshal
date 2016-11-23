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


class EnumDecoder(Decoder):

    def decode(self, data):
        v = super(EnumDecoder, self).decode(data)
        self.set_property(v, 'value', data.get('value'))
        return v
