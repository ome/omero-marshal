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

import importlib
import pkgutil
import logging
import re
from encode import encoders
from decode import decoders
from distutils.version import StrictVersion
from omero_version import omero_version

logger = logging.getLogger('omero-marshal')


ENCODERS = dict()
DECODERS = dict()


def dumps(obj):
    pass


def get_encoder(t):
    try:
        return ENCODERS[t]
    except KeyError:
        logger.warn('Requested unknown encoder %s' % t, exc_info=True)
        return None


def get_decoder(t):
    try:
        return DECODERS[t]
    except KeyError:
        logger.warn('Requested unknown decoder %s' % t, exc_info=True)
        return None


VERSION_REGEXP = re.compile(r'^(\d+\.\d+\.\d+)')


def get_schema_version(version):
    m = VERSION_REGEXP.search(version)
    if m is None:
        raise Exception("Invalid OMERO version number: " + version)
    v = StrictVersion(m.group(1))
    if v >= StrictVersion('5.1.0') and v < StrictVersion('5.3.0'):
        return '2015-01'
    elif v >= StrictVersion('5.3.0') and v < StrictVersion('6.0.0'):
        return '2016-06'
    else:
        raise Exception("Unsupported OMERO version: " + version)


SCHEMA_VERSION = get_schema_version(omero_version)
BASE_URL = 'http://www.openmicroscopy.org/Schemas'
if SCHEMA_VERSION == "2015-01":
    ROI_NS = 'ROI'
    SA_NS = 'SA'
    SPW_NS = 'SPW'
else:
    ROI_NS = 'OME'
    SA_NS = 'OME'
    SPW_NS = 'OME'
OME_SCHEMA_URL = '%s/OME/%s' % (BASE_URL, SCHEMA_VERSION)
ROI_SCHEMA_URL = '%s/%s/%s' % (BASE_URL, ROI_NS, SCHEMA_VERSION)
SA_SCHEMA_URL = '%s/%s/%s' % (BASE_URL, SA_NS, SCHEMA_VERSION)
SPW_SCHEMA_URL = '%s/%s/%s' % (BASE_URL, SPW_NS, SCHEMA_VERSION)


class MarshallingCtx(object):

    def __init__(self, encoders, decoders):
        self.encoders = encoders
        self.decoders = decoders

    def get_encoder(self, t):
        try:
            return self.encoders[t]
        except KeyError:
            logger.warn('Requested unknown encoder %s' % t, exc_info=True)
            return None

    def get_decoder(self, t):
        try:
            return self.decoders[t]
        except KeyError:
            logger.warn('Requested unknown decoder %s' % t, exc_info=True)
            return None


_ctx = MarshallingCtx(ENCODERS, DECODERS)

packages = pkgutil.walk_packages(encoders.__path__, encoders.__name__ + '.')
for module_loader, name, ispkg in packages:
    m = importlib.import_module(name)
    try:
        t, encoder = m.encoder
        ENCODERS[t] = encoder(_ctx)
    except AttributeError:
        pass

packages = pkgutil.walk_packages(decoders.__path__, decoders.__name__ + '.')
for module_loader, name, ispkg in packages:
    m = importlib.import_module(name)
    try:
        t, decoder = m.decoder
        DECODERS[t] = decoder(_ctx)
    except AttributeError:
        pass
