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

from .shape import ShapeEncoder
from omero.model import LineI


class LineEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Line'

    def encode(self, obj):
        v = super(LineEncoder, self).encode(obj)
        self.set_if_not_none(v, 'X1', obj.x1)
        self.set_if_not_none(v, 'Y1', obj.y1)
        self.set_if_not_none(v, 'X2', obj.x2)
        self.set_if_not_none(v, 'Y2', obj.y2)
        return v

encoder = (LineI, LineEncoder)
