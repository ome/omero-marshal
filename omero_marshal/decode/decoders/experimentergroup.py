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

from .. import Decoder
from omero.model import ExperimenterGroupI


class ExperimenterGroupDecoder(Decoder):

    TYPE = \
        'http://www.openmicroscopy.org/Schemas/OME/2015-01#ExperimenterGroup'

    OMERO_CLASS = ExperimenterGroupI

    def decode(self, data):
        v = super(ExperimenterGroupDecoder, self).decode(data)
        v.description = self.to_rtype(data.get('Description'))
        v.name = self.to_rtype(data.get('Name'))
        return v

decoder = (ExperimenterGroupDecoder.TYPE, ExperimenterGroupDecoder)
