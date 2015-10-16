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

from .annotation import AnnotatableDecoder
from omero.model import RoiI


class RoiDecoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'

    OMERO_CLASS = RoiI

    def decode(self, data):
        v = super(RoiDecoder, self).decode(data)
        v.name = self.to_rtype(data.get('Name'))
        v.description = self.to_rtype(data.get('Description'))
        for shape in data.get('shapes', list()):
            shape_decoder = self.ctx.get_decoder(shape['@type'])
            v.addShape(shape_decoder.decode(shape))
        return v

decoder = (RoiDecoder.TYPE, RoiDecoder)
