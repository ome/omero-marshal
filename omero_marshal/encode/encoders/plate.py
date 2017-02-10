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
from .annotation import AnnotatableEncoder
from omero.model import PlateI


class Plate201501Encoder(AnnotatableEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#Plate'

    def encode(self, obj):
        v = super(Plate201501Encoder, self).encode(obj)
        self.set_if_not_none(v, 'Name', obj.name)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'ColumnNamingConvention',
                             obj.columnNamingConvention)
        self.set_if_not_none(v, 'RowNamingConvention',
                             obj.rowNamingConvention)
        self.set_if_not_none(v, 'Columns', obj.columns)
        self.set_if_not_none(v, 'Rows', obj.rows)
        self.set_if_not_none(v, 'FieldIndex', obj.defaultSample)
        self.set_if_not_none(v, 'ExternalIdentifier', obj.externalIdentifier)
        self.set_if_not_none(v, 'Status', obj.status)
        self.set_if_not_none(v, 'WellOriginX', obj.wellOriginX)
        self.set_if_not_none(v, 'WellOriginY', obj.wellOriginY)

        if obj.isWellsLoaded() and obj.sizeOfWells() > 0:
            wells = list()
            for well in obj.copyWells():
                well_encoder = self.ctx.get_encoder(well.__class__)
                wells.append(
                    well_encoder.encode(well)
                )
            v['Wells'] = wells
        return v


class Plate201606Encoder(Plate201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Plate'


if SCHEMA_VERSION == '2015-01':
    encoder = (PlateI, Plate201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (PlateI, Plate201606Encoder)
PlateEncoder = encoder[1]
