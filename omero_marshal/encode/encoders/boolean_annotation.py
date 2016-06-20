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

from ... import SCHEMA_VERSION
from .annotation import AnnotationEncoder
from omero.model import BooleanAnnotationI


class BooleanAnnotation201501Encoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#BooleanAnnotation'

    def encode(self, obj):
        v = super(BooleanAnnotation201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Value', obj.boolValue)
        return v


class BooleanAnnotation201606Encoder(BooleanAnnotation201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
        '#BooleanAnnotation'


if SCHEMA_VERSION == '2015-01':
    encoder = (BooleanAnnotationI, BooleanAnnotation201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (BooleanAnnotationI, BooleanAnnotation201606Encoder)
BooleanAnnotationEncoder = encoder[1]
