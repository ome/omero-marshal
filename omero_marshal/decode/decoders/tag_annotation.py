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
from .text_annotation import TextAnnotationDecoder
from omero.model import TagAnnotationI


class TagAnnotation201501Decoder(TextAnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#TagAnnotation'

    OMERO_CLASS = TagAnnotationI

    def decode(self, data):
        v = super(TagAnnotation201501Decoder, self).decode(data)
        return v


class TagAnnotation201606Decoder(TagAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#TagAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (TagAnnotation201501Decoder.TYPE,
               TagAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (TagAnnotation201606Decoder.TYPE,
               TagAnnotation201606Decoder)
TagAnnotationDecoder = decoder[1]
