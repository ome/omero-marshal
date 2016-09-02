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

from ... import SCHEMA_VERSION
from .shape import ShapeDecoder
from omero.model import LabelI


class Label201501Decoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Label'

    OMERO_CLASS = LabelI

    def decode(self, data):
        v = super(Label201501Decoder, self).decode(data)
        self.set_property(v, 'x', data.get('X'))
        self.set_property(v, 'y', data.get('Y'))
        return v


class Label201606Decoder(Label201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Label'


if SCHEMA_VERSION == '2015-01':
    decoder = (Label201501Decoder.TYPE, Label201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Label201606Decoder.TYPE, Label201606Decoder)
LabelDecoder = decoder[1]
