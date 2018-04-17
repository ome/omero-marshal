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
from omero.model import PermissionsI


class PermissionsDecoder(Decoder):

    TYPE = 'TBD#Permissions'

    OMERO_CLASS = PermissionsI

    def decode(self, data):
        o = PermissionsI()
        o.from_string(data['perm'])
        o._restrictions = [
            not data['canLink'], not data['canEdit'],
            not data['canDelete'], not data['canAnnotate']
        ]
        return o


decoder = (PermissionsDecoder.TYPE, PermissionsDecoder)
