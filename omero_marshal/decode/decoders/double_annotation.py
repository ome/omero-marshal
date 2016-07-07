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
from omero.model import DoubleAnnotationI


class DoubleAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#DoubleAnnotation'

    OMERO_CLASS = DoubleAnnotationI

    def decode(self, data):
        v = super(DoubleAnnotation201501Decoder, self).decode(data)
        self.set_property(v, 'doubleValue', data.get('Value'))
        return v


class DoubleAnnotation201606Decoder(DoubleAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#' \
        'DoubleAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (DoubleAnnotation201501Decoder.TYPE,
               DoubleAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (DoubleAnnotation201606Decoder.TYPE,
               DoubleAnnotation201606Decoder)
DoubleAnnotationDecoder = decoder[1]
