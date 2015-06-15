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

from .. import Encoder
from omero.model import RoiI


class RoiEncoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI'

    def encode(self, obj):
        v = super(RoiEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.description)
        return v

encoder = (RoiI, RoiEncoder)
