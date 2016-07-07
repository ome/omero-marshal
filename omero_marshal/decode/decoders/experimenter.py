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
from omero.model import ExperimenterI


class ExperimenterDecoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Experimenter'

    OMERO_CLASS = ExperimenterI

    def decode(self, data):
        v = super(ExperimenterDecoder, self).decode(data)
        self.set_property(v, 'firstName', data.get('FirstName'))
        self.set_property(v, 'middleName', data.get('MiddleName'))
        self.set_property(v, 'lastName', data.get('LastName'))
        self.set_property(v, 'email', data.get('Email'))
        self.set_property(v, 'institution', data.get('Institution'))
        self.set_property(v, 'omeName', data.get('UserName'))
        return v

decoder = (ExperimenterDecoder.TYPE, ExperimenterDecoder)
