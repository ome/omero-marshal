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
from .shape import ShapeEncoder
from omero.model import MaskI


class Mask201501Encoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Mask'

    def encode(self, obj):
        v = super(Mask201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.x)
        self.set_if_not_none(v, 'Y', obj.y)
        self.set_if_not_none(v, 'Width', obj.width)
        self.set_if_not_none(v, 'Height', obj.height)
        return v


class Mask201606Encoder(Mask201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Mask'


if SCHEMA_VERSION == '2015-01':
    encoder = (MaskI, Mask201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (MaskI, Mask201606Encoder)
MaskEncoder = encoder[1]
