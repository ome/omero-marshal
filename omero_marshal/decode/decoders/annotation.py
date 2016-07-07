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
from .. import Decoder
from omero.model import Annotation


class Annotation201501Decoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#Annotation'

    OMERO_CLASS = Annotation

    def decode(self, data):
        v = super(Annotation201501Decoder, self).decode(data)
        self.set_property(v, 'description', data.get('Description'))
        self.set_property(v, 'ns', data.get('Namespace'))
        return v


class Annotation201606Decoder(Annotation201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Annotation'


class Annotatable201501Decoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#AnnotationRef'

    OMERO_CLASS = Annotation

    def decode(self, data):
        v = super(Annotatable201501Decoder, self).decode(data)
        if 'Annotations' in data:
            for annotation in data['Annotations']:
                annotation_decoder = self.ctx.get_decoder(annotation['@type'])
                v.linkAnnotation(annotation_decoder.decode(annotation))
        else:
            v.unloadAnnotationLinks()
        return v


class Annotatable201606Decoder(Annotatable201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#AnnotationRef'


if SCHEMA_VERSION == '2015-01':
    decoder = (Annotation201501Decoder.TYPE, Annotation201501Decoder)
    AnnotatableDecoder = Annotatable201501Decoder
elif SCHEMA_VERSION == '2016-06':
    decoder = (Annotation201606Decoder.TYPE, Annotation201606Decoder)
    AnnotatableDecoder = Annotatable201606Decoder
AnnotationDecoder = decoder[1]
