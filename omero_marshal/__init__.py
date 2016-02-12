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
from encode import encoders
from decode import decoders


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
