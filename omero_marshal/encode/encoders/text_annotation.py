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

from .annotation import AnnotationEncoder
from omero.model import TextAnnotation


class TextAnnotationEncoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TextAnnotation'

    def encode(self, obj):
        v = super(TextAnnotationEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Value', obj.textValue)
        return v

encoder = (TextAnnotation, TextAnnotationEncoder)
