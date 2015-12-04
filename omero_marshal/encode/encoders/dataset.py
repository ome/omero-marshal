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
from omero.model import DatasetI


class DatasetEncoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Dataset'

    def encode(self, obj):
        v = super(DatasetEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        return v

encoder = (DatasetI, DatasetEncoder)
