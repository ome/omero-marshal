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
from .. import Encoder
from omero.model import ExperimenterGroupI


class ExperimenterGroup201501Encoder(Encoder):

    TYPE = \
        'http://www.openmicroscopy.org/Schemas/OME/2015-01#ExperimenterGroup'

    def encode(self, obj):
        v = super(ExperimenterGroup201501Encoder, self).encode(obj)
        if not obj.isLoaded():
            return v
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'Name', obj.name)

        if obj.isGroupExperimenterMapLoaded() \
                and obj.sizeOfGroupExperimenterMap() > 0:
            experimenters = list()
            for group_experimenter_map in obj.copyGroupExperimenterMap():
                experimenter = group_experimenter_map.child
                experimenter_encoder = self.ctx.get_encoder(
                    experimenter.__class__
                )
                experimenter_data = experimenter_encoder.encode(experimenter)
                self.set_if_not_none(
                    experimenter_data,
                    'omero:owner',
                    group_experimenter_map.owner
                )
                experimenters.append(experimenter_data)
            v['Experimenters'] = experimenters
        return v


class ExperimenterGroup201606Encoder(ExperimenterGroup201501Encoder):

    TYPE = \
        'http://www.openmicroscopy.org/Schemas/OME/2016-06#ExperimenterGroup'


if SCHEMA_VERSION == '2015-01':
    encoder = (ExperimenterGroupI, ExperimenterGroup201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (ExperimenterGroupI, ExperimenterGroup201606Encoder)
ExperimenterGroupEncoder = encoder[1]
