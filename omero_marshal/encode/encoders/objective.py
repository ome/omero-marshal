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
from omero.model import ObjectiveI


class Objective201501Encoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Objective'

    def encode(self, obj):
        v = super(Objective201501Encoder, self).encode(obj)
        if not obj.isLoaded():
            return v
        self.set_if_not_none(v, 'LensNA', obj.lensNA)
        self.set_if_not_none(v, 'Iris', obj.iris)
        self.set_if_not_none(v, 'LotNumber', obj.lotNumber)
        self.set_if_not_none(v, 'Manufacturer', obj.manufacturer)
        self.set_if_not_none(v, 'Model', obj.model)
        self.set_if_not_none(v, 'NominalMagnification',
                             obj.nominalMagnification)
        self.set_if_not_none(v, 'SerialNumber', obj.serialNumber)
        self.set_if_not_none(v, 'WorkingDistance', obj.workingDistance)
        # enums
        for attr in ["Correction", "Immersion"]:
            enum_value = getattr(obj, attr.lower())
            if enum_value is not None:
                enum_encoder = self.ctx.get_encoder(enum_value.__class__)
                v[attr] = enum_encoder.encode(enum_value)
        return v


class Objective201606Encoder(Objective201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Objective'


if SCHEMA_VERSION == '2015-01':
    encoder = (ObjectiveI, Objective201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (ObjectiveI, Objective201606Encoder)
ObjectiveEncoder = encoder[1]
