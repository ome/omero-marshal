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
from omero.model import MapAnnotationI


class MapAnnotationEncoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#MapAnnotation'

    def encode(self, obj):
        v = super(MapAnnotationEncoder, self).encode(obj)
        if obj.mapValue is None:
            return None
        self.set_if_not_none(
            v, 'Value', [
                [nv.name, nv.value] for nv in obj.getMapValue()
            ]
        )
        return v

encoder = (MapAnnotationI, MapAnnotationEncoder)
