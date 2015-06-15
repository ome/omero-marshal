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
from encode import encoders
from decode import decoders


ENCODERS = dict()
DECODERS = dict()


def dumps(obj):
    pass


def get_encoder(t):
    return ENCODERS.get(t)


def get_decoder(t):
    return DECODERS.get(t)


packages = pkgutil.walk_packages(encoders.__path__, encoders.__name__ + '.')
for module_loader, name, ispkg in packages:
    m = importlib.import_module(name)
    try:
        t, encoder = m.encoder
        ENCODERS[t] = encoder
    except AttributeError:
        pass

packages = pkgutil.walk_packages(decoders.__path__, decoders.__name__ + '.')
for module_loader, name, ispkg in packages:
    m = importlib.import_module(name)
    try:
        t, decoder = m.decoder
        DECODERS[t] = decoder
    except AttributeError:
        pass
