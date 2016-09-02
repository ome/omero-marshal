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
from omero.model import TermAnnotationI


class TermAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#TermAnnotation'

    OMERO_CLASS = TermAnnotationI

    def decode(self, data):
        v = super(TermAnnotation201501Decoder, self).decode(data)
        self.set_property(v, 'termValue', data.get('Value'))
        return v


class TermAnnotation201606Decoder(TermAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#TermAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (TermAnnotation201501Decoder.TYPE,
               TermAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (TermAnnotation201606Decoder.TYPE,
               TermAnnotation201606Decoder)
TermAnnotationDecoder = decoder[1]
