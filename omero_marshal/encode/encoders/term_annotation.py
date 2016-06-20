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
from .annotation import AnnotationEncoder
from omero.model import TermAnnotationI


class TermAnnotation201501Encoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TermAnnotation'

    def encode(self, obj):
        v = super(TermAnnotation201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Value', obj.termValue)
        return v


class TermAnnotation201606Encoder(TermAnnotation201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
        '#TermAnnotation'


if SCHEMA_VERSION == '2015-01':
    encoder = (TermAnnotationI, TermAnnotation201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (TermAnnotationI, TermAnnotation201606Encoder)
TermAnnotationEncoder = encoder[1]
