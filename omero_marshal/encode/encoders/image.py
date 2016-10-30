#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from .annotation import AnnotatableEncoder
from omero.model import ImageI


class ImageEncoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Image'

    def encode(self, obj):
        v = super(ImageEncoder, self).encode(obj)
        self.set_if_not_none(v, 'AcquisitionDate', obj.acquisitionDate)
        self.set_if_not_none(v, 'omero:archived', obj.archived)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'omero:partial', obj.partial)
        if obj.format.isLoaded():
            format_encoder = self.ctx.get_encoder(obj.format.__class__)
            self.set_if_not_none(
                v, 'omero:format', format_encoder.encode(obj.format)
            )
        if obj.isPixelsLoaded() and obj.sizeOfPixels() > 0:
            pixels = obj.getPrimaryPixels()
            pixels_encoder = self.ctx.get_encoder(pixels.__class__)
            v['Pixels'] = pixels_encoder.encode(pixels)
        return v

encoder = (ImageI, ImageEncoder)
