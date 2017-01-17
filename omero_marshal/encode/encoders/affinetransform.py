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

from ... import SCHEMA_VERSION
from .. import Encoder

try:
    # Import transform classes introduced in OMERO 5.3.0
    from omero.model import AffineTransformI
except ImportError:
    # Use internal AffineTransformI classes for OMERO 5.1.x and OMERO 5.2.x
    from omero_marshal.legacy.affinetransform import AffineTransformI


class AffineTransform201501Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#AffineTransform'

    def encode(self, obj):
        v = super(AffineTransform201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'A00', obj.getA00())
        self.set_if_not_none(v, 'A10', obj.getA10())
        self.set_if_not_none(v, 'A01', obj.getA01())
        self.set_if_not_none(v, 'A11', obj.getA11())
        self.set_if_not_none(v, 'A02', obj.getA02())
        self.set_if_not_none(v, 'A12', obj.getA12())
        return v


class AffineTransform201606Encoder(AffineTransform201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#AffineTransform'


if SCHEMA_VERSION == '2015-01':
    encoder = (AffineTransformI, AffineTransform201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (AffineTransformI, AffineTransform201606Encoder)
AffineTransformEncoder = encoder[1]
