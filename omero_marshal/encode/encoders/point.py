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
from omero.model import PointI


class PointEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Point'

    def encode(self, obj):
        v = super(PointEncoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.cx)
        self.set_if_not_none(v, 'Y', obj.cy)
        return v

encoder = (PointI, PointEncoder)
