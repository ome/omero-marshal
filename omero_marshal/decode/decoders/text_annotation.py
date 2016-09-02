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
from omero.model import TextAnnotation


class TextAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#TextAnnotation'

    OMERO_CLASS = TextAnnotation

    def decode(self, data):
        v = super(TextAnnotation201501Decoder, self).decode(data)
        self.set_property(v, 'textValue', data.get('Value'))
        return v


class TextAnnotation201606Decoder(TextAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#TextAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (TextAnnotation201501Decoder.TYPE,
               TextAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (TextAnnotation201606Decoder.TYPE,
               TextAnnotation201606Decoder)
TextAnnotationDecoder = decoder[1]
