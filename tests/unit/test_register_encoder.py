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

from omero.model import RoiI
from omero_marshal import get_encoder


class TestRegisterEncoder(object):

    def test_roi_encoder_registered(self):
        assert get_encoder(RoiI) is not None
