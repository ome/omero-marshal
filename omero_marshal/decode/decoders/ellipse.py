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
from omero.model import EllipseI


class EllipseDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'

    OMERO_CLASS = EllipseI

    def decode(self, data):
        v = super(EllipseDecoder, self).decode(data)
        self.set_property(v, 'cx', data.get('X'))
        self.set_property(v, 'cy', data.get('Y'))
        self.set_property(v, 'rx', data.get('RadiusX'))
        self.set_property(v, 'ry', data.get('RadiusY'))
        return v

decoder = (EllipseDecoder.TYPE, EllipseDecoder)
