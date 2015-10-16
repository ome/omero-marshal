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

from .text_annotation import TextAnnotationEncoder
from omero.model import TagAnnotationI


class TagAnnotationEncoder(TextAnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TagAnnotation'

    def encode(self, obj):
        v = super(TagAnnotationEncoder, self).encode(obj)
        return v

encoder = (TagAnnotationI, TagAnnotationEncoder)
