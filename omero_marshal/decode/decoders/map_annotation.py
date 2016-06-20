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
from .annotation import AnnotationDecoder
from omero.model import MapAnnotationI, NamedValue


class MapAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#MapAnnotation'

    OMERO_CLASS = MapAnnotationI

    def decode(self, data):
        v = super(MapAnnotation201501Decoder, self).decode(data)
        map_value = data.get('Value', list())
        map_value = [
            NamedValue(key, value) for key, value in map_value
        ]
        v.setMapValue(map_value)
        return v


class MapAnnotation201606Decoder(MapAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#MapAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (MapAnnotation201501Decoder.TYPE,
               MapAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (MapAnnotation201606Decoder.TYPE,
               MapAnnotation201606Decoder)
MapAnnotationDecoder = decoder[1]
