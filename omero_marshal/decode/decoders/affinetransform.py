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
from .. import Decoder

try:
    # Import transform classes introduced in OMERO 5.3.0
    from omero.model import AffineTransformI
except ImportError:
    # Use internal AffineTransformI classes for OMERO 5.2.x
    from omero_marshal.legacy.affinetransform import AffineTransformI
from omero.rtypes import rdouble


class AffineTransform201501Decoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#AffineTransform'

    OMERO_CLASS = AffineTransformI

    def decode(self, data):
        t = super(AffineTransform201501Decoder, self).decode(data)
        t.setA00(rdouble(data['A00']))
        t.setA10(rdouble(data['A10']))
        t.setA01(rdouble(data['A01']))
        t.setA11(rdouble(data['A11']))
        t.setA02(rdouble(data['A02']))
        t.setA12(rdouble(data['A12']))
        return t


class AffineTransform201606Decoder(AffineTransform201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#AffineTransform'

    def set_transform(self, data):
        return data


if SCHEMA_VERSION == '2015-01':
    decoder = (AffineTransform201501Decoder.TYPE, AffineTransform201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (AffineTransform201606Decoder.TYPE, AffineTransform201606Decoder)
AffineTransformDecoder = decoder[1]
