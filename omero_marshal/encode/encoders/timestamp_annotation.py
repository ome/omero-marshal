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
from omero.model import TimestampAnnotationI


class TimestampAnnotation201501Encoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TimestampAnnotation'

    def encode(self, obj, include_context=None):
        v = super(TimestampAnnotation201501Encoder, self).encode(obj, include_context)
        self.set_if_not_none(v, 'Value', obj.timeValue)
        return v


class TimestampAnnotation201606Encoder(TimestampAnnotation201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
        '#TimestampAnnotation'


if SCHEMA_VERSION == '2015-01':
    encoder = (TimestampAnnotationI, TimestampAnnotation201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (TimestampAnnotationI, TimestampAnnotation201606Encoder)
TimestampAnnotationEncoder = encoder[1]
