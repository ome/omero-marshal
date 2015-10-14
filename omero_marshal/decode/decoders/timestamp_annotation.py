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
from omero.model import TimestampAnnotationI

from omero.rtypes import RTimeI


class TimestampAnnotationDecoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#TimestampAnnotation'

    OMERO_CLASS = TimestampAnnotationI

    def decode(self, data):
        v = super(TimestampAnnotationDecoder, self).decode(data)
        time_value = data.get('Value')
        if time_value is not None:
            time_value = RTimeI(time_value)
        v.timeValue = time_value
        return v

decoder = (TimestampAnnotationDecoder.TYPE, TimestampAnnotationDecoder)
