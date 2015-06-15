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
from omero.model import EllipseI


class EllipseEncoder(ShapeEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'

    def encode(self, obj):
        v = super(EllipseEncoder, self).encode(obj)
        self.set_if_not_none(v, 'X', obj.cx)
        self.set_if_not_none(v, 'Y', obj.cy)
        self.set_if_not_none(v, 'RadiusX', obj.rx)
        self.set_if_not_none(v, 'RadiusY', obj.ry)
        return v

encoder = (EllipseI, EllipseEncoder)
