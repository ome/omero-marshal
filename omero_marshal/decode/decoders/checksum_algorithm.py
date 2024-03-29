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

from .enum import EnumDecoder
from omero.model import ChecksumAlgorithmI


class ChecksumAlgorithmDecoder(EnumDecoder):

    TYPE = 'TBD#ChecksumAlgorithm'

    OMERO_CLASS = ChecksumAlgorithmI


decoder = (ChecksumAlgorithmDecoder.TYPE, ChecksumAlgorithmDecoder)
