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
from omero.model import TermAnnotationI


class TermAnnotationEncoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TermAnnotation'

    def encode(self, obj):
        v = super(TermAnnotationEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Value', obj.termValue)
        return v

encoder = (TermAnnotationI, TermAnnotationEncoder)
