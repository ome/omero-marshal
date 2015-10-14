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
from omero.model import Annotation


class AnnotationDecoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#Annotation'

    OMERO_CLASS = Annotation

    def decode(self, data):
        v = super(AnnotationDecoder, self).decode(data)
        v.description = self.to_rtype(data.get('Description'))
        v.ns = self.to_rtype(data.get('Namespace'))
        return v


class AnnotatableDecoder(Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#AnnotationRef'

    OMERO_CLASS = Annotation

    def decode(self, data):
        v = super(AnnotatableDecoder, self).decode(data)
        if 'Annotations' in data:
            for annotation in data['Annotations']:
                annotation_decoder = self.ctx.get_decoder(annotation['@type'])
                v.linkAnnotation(annotation_decoder.decode(annotation))
        else:
            v.unloadAnnotationLinks()
        return v


decoder = (AnnotationDecoder.TYPE, AnnotationDecoder)
