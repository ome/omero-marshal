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
        v.firstName = self.to_rtype(data.get('FirstName'))
        v.middleName = self.to_rtype(data.get('MiddleName'))
        v.lastName = self.to_rtype(data.get('LastName'))
        v.email = self.to_rtype(data.get('Email'))
        v.institution = self.to_rtype(data.get('Institution'))
        v.omeName = self.to_rtype(data.get('UserName'))
        return v

decoder = (ExperimenterDecoder.TYPE, ExperimenterDecoder)
