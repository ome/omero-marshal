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

from .annotation import AnnotationDecoder
from omero.model import DoubleAnnotationI


class DoubleAnnotationDecoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#DoubleAnnotation'

    OMERO_CLASS = DoubleAnnotationI

    def decode(self, data):
        v = super(DoubleAnnotationDecoder, self).decode(data)
        v.doubleValue = self.to_rtype(data.get('Value'))
        return v

decoder = (DoubleAnnotationDecoder.TYPE, DoubleAnnotationDecoder)
