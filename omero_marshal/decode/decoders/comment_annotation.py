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
from omero.model import CommentAnnotationI


class CommentAnnotation201501Decoder(TextAnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#CommentAnnotation'

    OMERO_CLASS = CommentAnnotationI

    def decode(self, data):
        v = super(CommentAnnotation201501Decoder, self).decode(data)
        return v


class CommentAnnotation201606Decoder(CommentAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#' \
        'CommentAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (CommentAnnotation201501Decoder.TYPE,
               CommentAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (CommentAnnotation201606Decoder.TYPE,
               CommentAnnotation201606Decoder)
CommentAnnotationDecoder = decoder[1]
