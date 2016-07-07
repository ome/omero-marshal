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
from omero.model import LongAnnotationI


class LongAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#LongAnnotation'

    OMERO_CLASS = LongAnnotationI

    def decode(self, data):
        v = super(LongAnnotation201501Decoder, self).decode(data)
        self.set_property(v, 'longValue', data.get('Value'))
        return v


class LongAnnotation201606Decoder(LongAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#LongAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (LongAnnotation201501Decoder.TYPE,
               LongAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (LongAnnotation201606Decoder.TYPE,
               LongAnnotation201606Decoder)
LongAnnotationDecoder = decoder[1]
