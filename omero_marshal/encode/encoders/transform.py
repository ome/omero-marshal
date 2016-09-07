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

from .annotation import Encoder
try:
    from omero.model import AffineTransformI
except ImportError:
    pass


class Transform201606Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#AffineTransform'

    def encode(self, obj):
        v = super(Transform201606Encoder, self).encode(obj)
        self.set_if_not_none(v, 'A00', obj.getA00())
        self.set_if_not_none(v, 'A10', obj.getA10())
        self.set_if_not_none(v, 'A01', obj.getA01())
        self.set_if_not_none(v, 'A11', obj.getA11())
        self.set_if_not_none(v, 'A02', obj.getA02())
        self.set_if_not_none(v, 'A12', obj.getA12())
        return v


encoder = (AffineTransformI, Transform201606Encoder)
TransformEncoder = encoder[1]
