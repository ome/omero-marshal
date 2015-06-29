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

from .shape import ShapeDecoder
from omero.model import RectI


class RectDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Rectangle'

    OMERO_CLASS = RectI

    def decode(self, data):
        v = super(RectDecoder, self).decode(data)
        v.x = self.to_rtype(data.get('X'))
        v.y = self.to_rtype(data.get('Y'))
        v.width = self.to_rtype(data.get('Width'))
        v.height = self.to_rtype(data.get('Height'))
        return v

decoder = (RectDecoder.TYPE, RectDecoder)
