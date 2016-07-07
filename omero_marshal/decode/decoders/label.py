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
from omero.model import LabelI


class LabelDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Label'

    OMERO_CLASS = LabelI

    def decode(self, data):
        v = super(LabelDecoder, self).decode(data)
        self.set_property(v, 'x', data.get('X'))
        self.set_property(v, 'y', data.get('Y'))
        return v

decoder = (LabelDecoder.TYPE, LabelDecoder)
