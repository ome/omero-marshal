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

from .. import Encoder
from omero.model import ExternalInfoI


class ExternalInfoEncoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OMERO/2016-06#ExternalInfo'

    def encode(self, obj, include_context=None):
        # Never include contexts for these objects
        v = super(ExternalInfoEncoder, self).encode(obj, False)
        if not obj.isLoaded():
            return v
        self.set_if_not_none(v, 'EntityId', obj.entityId)
        self.set_if_not_none(v, 'EntityType', obj.entityType)
        self.set_if_not_none(v, 'Lsid', obj.lsid)
        self.set_if_not_none(v, 'Uuid', obj.uuid)
        return v


encoder = (ExternalInfoI, ExternalInfoEncoder)
