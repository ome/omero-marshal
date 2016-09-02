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
from omero.model import BooleanAnnotationI


class BooleanAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#BooleanAnnotation'

    OMERO_CLASS = BooleanAnnotationI

    def decode(self, data):
        v = super(BooleanAnnotation201501Decoder, self).decode(data)
        self.set_property(v, 'boolValue', data.get('Value'))
        return v


class BooleanAnnotation201606Decoder(BooleanAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#' \
        'BooleanAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (BooleanAnnotation201501Decoder.TYPE,
               BooleanAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (BooleanAnnotation201606Decoder.TYPE,
               BooleanAnnotation201606Decoder)
BooleanAnnotationDecoder = decoder[1]
