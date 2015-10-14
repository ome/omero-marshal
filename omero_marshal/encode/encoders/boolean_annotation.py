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
from omero.model import BooleanAnnotationI


class BooleanAnnotationEncoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#BooleanAnnotation'

    def encode(self, obj):
        v = super(BooleanAnnotationEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Value', obj.boolValue)
        return v

encoder = (BooleanAnnotationI, BooleanAnnotationEncoder)
