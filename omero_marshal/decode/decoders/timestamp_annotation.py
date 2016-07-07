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
from .annotation import AnnotationDecoder
from omero.model import TimestampAnnotationI


class TimestampAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TimestampAnnotation'

    OMERO_CLASS = TimestampAnnotationI

    def decode(self, data):
        v = super(TimestampAnnotation201501Decoder, self).decode(data)
        self.set_property(v, 'timeValue', data.get('Value'))
        return v


class TimestampAnnotation201606Decoder(TimestampAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#' \
        'TimestampAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (TimestampAnnotation201501Decoder.TYPE,
               TimestampAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (TimestampAnnotation201606Decoder.TYPE,
               TimestampAnnotation201606Decoder)
TimestampAnnotationDecoder = decoder[1]
