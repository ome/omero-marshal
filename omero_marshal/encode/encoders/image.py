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
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'AcquisitionDate', obj.acquisitionDate)
        if obj.experiment is not None:
            pass
        if obj.isPixelsLoaded():
            pixels = []
            for pix in obj.copyPixels():
                pixels_encoder = self.ctx.get_encoder(pix.__class__)
                pixels.append(pixels_encoder.encode(pix))
            v['Pixels'] = pixels
        return v

encoder = (ImageI, ImageEncoder)
