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
from .. import Decoder
from omero.model import ExperimenterGroupI


class ExperimenterGroup201501Decoder(Decoder):

    TYPE = \
        'http://www.openmicroscopy.org/Schemas/OME/2015-01#ExperimenterGroup'

    OMERO_CLASS = ExperimenterGroupI

    def decode(self, data):
        v = super(ExperimenterGroup201501Decoder, self).decode(data)
        self.set_property(v, 'description', data.get('Description'))
        self.set_property(v, 'name', data.get('Name'))
        return v


class ExperimenterGroup201606Decoder(ExperimenterGroup201501Decoder):

    TYPE = \
        'http://www.openmicroscopy.org/Schemas/OME/2016-06#ExperimenterGroup'


if SCHEMA_VERSION == '2015-01':
    decoder = (ExperimenterGroup201501Decoder.TYPE,
               ExperimenterGroup201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (ExperimenterGroup201606Decoder.TYPE,
               ExperimenterGroup201606Decoder)
ExperimenterGroupDecoder = decoder[1]
