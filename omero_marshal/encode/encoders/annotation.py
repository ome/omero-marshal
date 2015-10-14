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
from omero.model import Annotation


class AnnotationEncoder(Encoder):
    '''
    Annotation
        BasicAnnotation
            BooleanAnnotation
                BooleanAnnotationI
            NumericAnnotation
                DoubleAnnotation
                    DoubleAnnotationI
                LongAnnotation
                    LongAnnotationI
            TermAnnotation
                TermAnnotationI
            TimestampAnnotation
                TimestampAnnotationI
        ListAnnotation
            ListAnnotationI
        MapAnnotation
            MapAnnotationI
        TextAnnotation
            CommentAnnotation
                CommentAnnotationI
            TagAnnotation
                TagAnnotationI
            XmlAnnotation
                XmlAnnotationI
        TypeAnnotation
            FileAnnotation
                FileAnnotationI
    '''

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#Annotation'

    def encode(self, obj):
        v = super(AnnotationEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'Namespace', obj.ns)
        return v

encoder = (Annotation, AnnotationEncoder)
