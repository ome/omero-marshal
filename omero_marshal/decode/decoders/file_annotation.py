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
from .annotation import AnnotationDecoder
from omero.model import FileAnnotationI


class FileAnnotation201501Decoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#FileAnnotation'

    OMERO_CLASS = FileAnnotationI

    def decode(self, data):
        v = super(FileAnnotation201501Decoder, self).decode(data)
        original_file = data.get('File')
        if original_file is not None:
            original_file_decoder = self.ctx.get_decoder(
                original_file['@type']
            )
            v.file = original_file_decoder.decode(
                original_file
            )
        return v


class FileAnnotation201606Decoder(FileAnnotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#' \
        'FileAnnotation'


if SCHEMA_VERSION == '2015-01':
    decoder = (FileAnnotation201501Decoder.TYPE,
               FileAnnotation201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (FileAnnotation201606Decoder.TYPE,
               FileAnnotation201606Decoder)
FileAnnotationDecoder = decoder[1]
