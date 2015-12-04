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

from .annotation import AnnotatableDecoder
from omero.model import DatasetI


class DatasetDecoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Dataset'

    OMERO_CLASS = DatasetI

    def decode(self, data):
        v = super(DatasetDecoder, self).decode(data)
        v.name = self.to_rtype(data.get('Name'))
        v.description = self.to_rtype(data.get('Description'))
        return v

decoder = (DatasetDecoder.TYPE, DatasetDecoder)
