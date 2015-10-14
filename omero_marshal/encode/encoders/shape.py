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

from .annotation import AnnotatableEncoder
from omero.model import Shape


class ShapeEncoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Shape'

    def encode(self, obj):
        v = super(ShapeEncoder, self).encode(obj)
        self.set_if_not_none(v, 'FillColor', obj.fillColor)
        self.set_if_not_none(v, 'FillRule', obj.fillRule)
        self.set_if_not_none(v, 'FontFamily', obj.fontFamily)
        self.set_if_not_none(v, 'FontSize', obj.fontSize)
        self.set_if_not_none(v, 'FontStyle', obj.fontStyle)
        self.set_if_not_none(v, 'LineCap', obj.strokeLineCap)
        self.set_if_not_none(v, 'Locked', obj.locked)
        self.set_if_not_none(v, 'StrokeColor', obj.strokeColor)
        self.set_if_not_none(v, 'StrokeDashArray', obj.strokeDashArray)
        self.set_if_not_none(v, 'StrokeWidth', obj.strokeWidth)
        self.set_if_not_none(v, 'Text', obj.textValue)
        self.set_if_not_none(v, 'TheC', obj.theC)
        self.set_if_not_none(v, 'TheT', obj.theT)
        self.set_if_not_none(v, 'TheZ', obj.theZ)
        self.set_if_not_none(v, 'Visible', obj.visibility)
        return v

encoder = (Shape, ShapeEncoder)
