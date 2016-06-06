#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from .. import Encoder
from omero.model import PixelsI


class PixelsEncoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Pixels'

    def encode(self, obj):
        v = super(PixelsEncoder, self).encode(obj)
        self.set_if_not_none(v, 'SizeX', obj.sizeX)
        self.set_if_not_none(v, 'SizeY', obj.sizeY)
        self.set_if_not_none(v, 'SizeZ', obj.sizeZ)
        self.set_if_not_none(v, 'SizeC', obj.sizeC)
        self.set_if_not_none(v, 'SizeT', obj.sizeT)

        return v

encoder = (PixelsI, PixelsEncoder)
