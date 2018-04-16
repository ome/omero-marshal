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
from omero.model import PermissionsI


class PermissionsEncoder(Encoder):

    TYPE = 'TBD#Permissions'

    def encode(self, obj):
        v = super(PermissionsEncoder, self).encode(obj)
        v['perm'] = str(obj)
        v['canAnnotate'] = obj.canAnnotate()
        v['canDelete'] = obj.canDelete()
        v['canEdit'] = obj.canEdit()
        v['canLink'] = obj.canLink()
        v['isWorldWrite'] = obj.isWorldWrite()
        v['isWorldRead'] = obj.isWorldRead()
        v['isGroupWrite'] = obj.isGroupWrite()
        v['isGroupRead'] = obj.isGroupRead()
        v['isGroupAnnotate'] = obj.isGroupAnnotate()
        v['isUserWrite'] = obj.isUserWrite()
        v['isUserRead'] = obj.isUserRead()
        return v


encoder = (PermissionsI, PermissionsEncoder)
