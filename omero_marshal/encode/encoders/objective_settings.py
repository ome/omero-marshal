#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from ... import SCHEMA_VERSION
from .. import Encoder
from omero.model import ObjectiveSettingsI


class ObjectiveSettings201501Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#ObjectiveSettings'

    def encode(self, obj):
        v = super(ObjectiveSettings201501Encoder, self).encode(obj)
        if not obj.isLoaded():
            return v
        self.set_if_not_none(v, 'CorrectionCollar', obj.correctionCollar)
        self.set_if_not_none(v, 'RefractiveIndex', obj.refractiveIndex)
        if obj.objective and obj.objective.isLoaded():
            objective_encoder = self.ctx.get_encoder(obj.objective.__class__)
            v['objective'] = objective_encoder.encode(obj.objective)
        return v


class ObjectiveSettings201606Encoder(ObjectiveSettings201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#ObjectiveSettings'


if SCHEMA_VERSION == '2015-01':
    encoder = (ObjectiveSettingsI, ObjectiveSettings201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (ObjectiveSettingsI, ObjectiveSettings201606Encoder)
ObjectiveSettingsEncoder = encoder[1]
