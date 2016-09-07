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

from omero.model import IObject


class AffineTransformI(IObject):

    A00 = "ome.model.roi.AffineTransform_a00"
    A10 = "ome.model.roi.AffineTransform_a10"
    A01 = "ome.model.roi.AffineTransform_a01"
    A11 = "ome.model.roi.AffineTransform_a11"
    A02 = "ome.model.roi.AffineTransform_a02"
    A12 = "ome.model.roi.AffineTransform_a12"
    DETAILS = None

    def __init__(self, transform):
        return
