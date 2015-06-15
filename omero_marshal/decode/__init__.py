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


class Decoder(object):

    TYPE = ''

    OMERO_CLASS = None

    def __init__(self, ctx):
        self.ctx = ctx

    def decode(self, data):
        return self.OMERO_CLASS(data.get('@id'))
