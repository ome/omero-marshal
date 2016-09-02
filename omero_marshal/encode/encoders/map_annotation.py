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
from omero.model import MapAnnotationI


class MapAnnotation201501Encoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#MapAnnotation'

    def encode(self, obj):
        v = super(MapAnnotation201501Encoder, self).encode(obj)
        if obj.mapValue is None:
            return None
        self.set_if_not_none(
            v, 'Value', [
                [nv.name, nv.value] for nv in obj.getMapValue()
            ]
        )
        return v


class MapAnnotation201606Encoder(MapAnnotation201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
        '#MapAnnotation'


if SCHEMA_VERSION == '2015-01':
    encoder = (MapAnnotationI, MapAnnotation201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (MapAnnotationI, MapAnnotation201606Encoder)
MapAnnotationEncoder = encoder[1]
