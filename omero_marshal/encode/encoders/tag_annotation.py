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
from .text_annotation import TextAnnotationEncoder
from omero.model import TagAnnotationI


class TagAnnotation201501Encoder(TextAnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TagAnnotation'

    def encode(self, obj):
        v = super(TagAnnotation201501Encoder, self).encode(obj)
        return v


class TagAnnotation201606Encoder(TagAnnotation201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
        '#TagAnnotation'


if SCHEMA_VERSION == '2015-01':
    encoder = (TagAnnotationI, TagAnnotation201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (TagAnnotationI, TagAnnotation201606Encoder)
TagAnnotationEncoder = encoder[1]
