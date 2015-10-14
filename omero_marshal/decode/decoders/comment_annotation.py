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

from .text_annotation import TextAnnotationDecoder
from omero.model import CommentAnnotationI


class CommentAnnotationDecoder(TextAnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#CommentAnnotation'

    OMERO_CLASS = CommentAnnotationI

    def decode(self, data):
        v = super(CommentAnnotationDecoder, self).decode(data)
        return v

decoder = (CommentAnnotationDecoder.TYPE, CommentAnnotationDecoder)
