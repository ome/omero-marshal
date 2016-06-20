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
from omero.model import XmlAnnotationI


class XmlAnnotation201501Decoder(TextAnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#XmlAnnotation'

    OMERO_CLASS = XmlAnnotationI

    def decode(self, data):
        v = super(XmlAnnotation201501Decoder, self).decode(data)
        return v


class XmlAnnotation201606Decoder(XmlAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#' \
        'XmlAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (XmlAnnotation201501Decoder.TYPE,
               XmlAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (XmlAnnotation201606Decoder.TYPE,
               XmlAnnotation201606Decoder)
XmlAnnotationDecoder = decoder[1]
