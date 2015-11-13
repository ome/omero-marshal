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
from omero.model import MapAnnotationI, NamedValue


class MapAnnotationDecoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#MapAnnotation'

    OMERO_CLASS = MapAnnotationI

    def decode(self, data):
        v = super(MapAnnotationDecoder, self).decode(data)
        map_value = data.get('Value', list())
        map_value = [
            NamedValue(key, value) for key, value in map_value
        ]
        v.setMapValue(map_value)
        return v

decoder = (MapAnnotationDecoder.TYPE, MapAnnotationDecoder)
