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
from .annotation import AnnotatableDecoder
from omero.model import PlateI


class Plate201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SPW/2015-01#Plate'

    OMERO_CLASS = PlateI

    def decode(self, data):
        v = super(Plate201501Decoder, self).decode(data)
        self.set_property(v, 'name', data.get('Name'))
        self.set_property(v, 'description', data.get('Description'))
        self.set_property(v, 'columnNamingConvention',
                          data.get('ColumnNamingConvention'))
        self.set_property(v, 'rowNamingConvention',
                          data.get('RowNamingConvention'))
        self.set_property(v, 'columns', data.get('Columns'))
        self.set_property(v, 'rows', data.get('Rows'))
        self.set_property(v, 'defaultSample', data.get('FieldIndex'))
        self.set_property(v, 'externalIdentifier',
                          data.get('ExternalIdentifier'))
        self.set_property(v, 'status', data.get('Status'))
        v.wellOriginX = self.to_unit(data.get('WellOriginX'))
        v.wellOriginY = self.to_unit(data.get('WellOriginY'))

        for well in data.get('Wells', list()):
            well_decoder = self.ctx.get_decoder(well['@type'])
            v.addWell(well_decoder.decode(well))
        return v


class Plate201606Decoder(Plate201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Plate'


if SCHEMA_VERSION == '2015-01':
    decoder = (Plate201501Decoder.TYPE, Plate201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Plate201606Decoder.TYPE, Plate201606Decoder)
PlateDecoder = decoder[1]
