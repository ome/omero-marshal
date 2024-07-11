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

import pytest

from omero.model import \
    AcquisitionModeI, \
    BooleanAnnotationI, \
    ChannelI, \
    ChecksumAlgorithmI, \
    CommentAnnotationI, \
    ContrastMethodI, \
    DatasetI, \
    DetailsI, \
    DimensionOrderI, \
    DoubleAnnotationI, \
    EllipseI, \
    ExperimenterI, \
    ExperimenterGroupI, \
    ExternalInfoI, \
    FileAnnotationI, \
    FormatI, \
    IlluminationI, \
    ImageI, \
    LabelI, \
    LengthI, \
    LineI, \
    LongAnnotationI, \
    LogicalChannelI, \
    OriginalFileI, \
    MapAnnotationI, \
    MaskI, \
    NamedValue, \
    TagAnnotationI, \
    TermAnnotationI, \
    TimestampAnnotationI, \
    XmlAnnotationI, \
    RoiI, \
    PermissionsI, \
    PhotometricInterpretationI, \
    PixelsI, \
    PixelsTypeI, \
    PlateI, \
    PlateAcquisitionI, \
    PointI, \
    PolygonI, \
    PolylineI, \
    ProjectI, \
    ScreenI, \
    TimeI, \
    WellI, \
    WellSampleI
from omero.model.enums import UnitsLength, UnitsTime
from omero.rtypes import rlong, rint, rstring, rdouble, rbool, rtime

# Handle differences in class naming between OMERO 5.1.x and 5.2.x
try:
    # OMERO 5.1.x
    from omero.model import RectI as RectangleI
except ImportError:
    # OMERO 5.2.x
    from omero.model import RectangleI

try:
    # Import transform classes introduced in OMERO 5.3.0
    from omero.model import AffineTransformI
except ImportError:
    # Use internal AffineTransformI classes for OMERO 5.1.x and OMERO 5.2.x
    from omero_marshal.legacy.affinetransform import AffineTransformI

from omero_marshal import SCHEMA_VERSION


def create_project(with_datasets=False, with_images=False):
    project = ProjectI()
    project.id = rlong(1)
    project.name = rstring('the_name')
    project.description = rstring('the_description')
    dataset_count = 2

    if not with_datasets:
        return project
    for dataset_id in range(0, dataset_count):
        dataset = DatasetI()
        dataset.id = rlong(dataset_id + 1)
        dataset.name = rstring('dataset_name_%d' % (dataset_id + 1))
        dataset.description = rstring(
            'dataset_description_%d' % (dataset_id + 1)
        )
        project.linkDataset(dataset)
        if not with_images:
            continue
        for image_id in range(1, 3):
            image_id = (dataset_id * dataset_count) + image_id
            dataset.linkImage(create_image(image_id))
    return project


def create_image(image_id, with_pixels=False):
    image_format = FormatI(1)
    image_format.value = rstring('PNG')

    image = ImageI()
    image.id = rlong(image_id)
    image.acquisitionDate = rtime(1)
    image.archived = rbool(False)
    image.description = rstring('image_description_%d' % image_id)
    image.name = rstring('image_name_%d' % image_id)
    image.partial = rbool(False)
    image.series = rint(0)
    image.format = image_format
    if not with_pixels:
        return image
    dimension_order = DimensionOrderI(1)
    dimension_order.value = rstring('XYZCT')
    pixels_type = PixelsTypeI(1)
    pixels_type.value = 'bit'

    pixels = PixelsI(1)
    pixels.methodology = rstring('methodology')
    pixels.physicalSizeX = LengthI(1.0, UnitsLength.MICROMETER)
    pixels.physicalSizeY = LengthI(2.0, UnitsLength.MICROMETER)
    pixels.physicalSizeZ = LengthI(3.0, UnitsLength.MICROMETER)
    pixels.sha1 = rstring('61ee8b5601a84d5154387578466c8998848ba089')
    pixels.significantBits = rint(16)
    pixels.sizeX = rint(1)
    pixels.sizeY = rint(2)
    pixels.sizeZ = rint(3)
    pixels.sizeC = rint(4)
    pixels.sizeT = rint(5)
    pixels.timeIncrement = TimeI(1.0, UnitsTime.MILLISECOND)
    pixels.waveIncrement = rdouble(2.0)
    pixels.waveStart = rint(1)
    pixels.dimensionOrder = dimension_order
    pixels.pixelsType = pixels_type
    image.addPixels(pixels)

    contrast_method = ContrastMethodI(8)
    contrast_method.value = rstring('Fluorescence')
    illumination = IlluminationI(1)
    illumination.value = rstring('Transmitted')
    acquisition_mode = AcquisitionModeI(1)
    acquisition_mode.value = rstring('WideField')
    photometric_interpretation = PhotometricInterpretationI(1)
    photometric_interpretation.value = rstring('RGB')

    channel_1 = ChannelI(1)
    channel_1.alpha = rint(255)
    channel_1.blue = rint(255)
    channel_1.green = rint(255)
    channel_1.red = rint(255)
    channel_1.lookupTable = rstring('rainbow')
    logical_channel_1 = LogicalChannelI(1)
    logical_channel_1.emissionWave = LengthI(509.0, UnitsLength.NANOMETER)
    logical_channel_1.excitationWave = LengthI(488.0, UnitsLength.NANOMETER)
    logical_channel_1.fluor = rstring('GFP')
    logical_channel_1.name = rstring('GFP/488')
    logical_channel_1.ndFilter = rdouble(1.0)
    logical_channel_1.pinHoleSize = LengthI(1.0, UnitsLength.NANOMETER)
    logical_channel_1.pockelCellSetting = rint(0)
    logical_channel_1.samplesPerPixel = rint(2)
    logical_channel_1.contrastMethod = contrast_method
    logical_channel_1.illumination = illumination
    logical_channel_1.mode = acquisition_mode
    logical_channel_1.photometricInterpretation = photometric_interpretation
    channel_1.logicalChannel = logical_channel_1

    channel_2 = ChannelI(2)
    channel_2.alpha = rint(255)
    channel_2.blue = rint(255)
    channel_2.green = rint(0)
    channel_2.red = rint(255)
    channel_2.lookupTable = rstring('rainbow')
    logical_channel_2 = LogicalChannelI(2)
    logical_channel_2.emissionWave = LengthI(470.0, UnitsLength.NANOMETER)
    logical_channel_2.excitationWave = LengthI(405.0, UnitsLength.NANOMETER)
    logical_channel_2.fluor = rstring('DAPI')
    logical_channel_2.name = rstring('DAPI/405')
    logical_channel_2.ndFilter = rdouble(1.0)
    logical_channel_2.pinHoleSize = LengthI(2.0, UnitsLength.NANOMETER)
    logical_channel_2.pockelCellSetting = rint(0)
    logical_channel_2.samplesPerPixel = rint(2)
    logical_channel_2.contrastMethod = contrast_method
    logical_channel_2.illumination = illumination
    logical_channel_2.mode = acquisition_mode
    logical_channel_2.photometricInterpretation = photometric_interpretation
    channel_2.logicalChannel = logical_channel_2

    pixels.addChannel(channel_1)
    pixels.addChannel(channel_2)
    return image


@pytest.fixture()
def project():
    return create_project()


@pytest.fixture()
def project_with_datasets(project):
    return create_project(with_datasets=True)


@pytest.fixture()
def project_with_datasets_and_images(project):
    return create_project(with_datasets=True, with_images=True)


@pytest.fixture()
def image():
    return create_image(1)


@pytest.fixture()
def image_pixels():
    return create_image(1, with_pixels=True)


@pytest.fixture()
def screen():
    o = ScreenI()
    o.id = rlong(4)
    o.name = rstring('the_name')
    o.description = rstring('the_description')
    o.protocolDescription = rstring('the_protocol_description')
    o.protocolIdentifier = rstring('the_protocol_identifier')
    o.reagentSetDescription = rstring('the_reagent_set_description')
    o.reagentSetIdentifier = rstring('the_reagent_set_identifier')
    o.type = rstring('the_type')
    return o


@pytest.fixture()
def well():
    """Basic Well for testing Color. Full test of Well below."""
    well = WellI()
    well.id = rlong(1)
    well.column = rint(0)
    well.row = rint(0)
    return well


@pytest.fixture()
def screen_with_plates(screen):
    for plate_id in range(5, 7):
        o = PlateI()
        o.id = rlong(plate_id)
        o.name = rstring('plate_name_%d' % plate_id)
        o.description = rstring('plate_description_%d' % plate_id)
        o.columnNamingConvention = rstring('number')
        o.rowNamingConvention = rstring('letter')
        o.columns = rint(12)
        o.rows = rint(8)
        o.defaultSample = rint(0)
        o.externalIdentifier = rstring('external_identifier_%d' % plate_id)
        o.status = rstring('status_%d' % plate_id)
        o.wellOriginX = LengthI(0.1, UnitsLength.REFERENCEFRAME)
        o.wellOriginY = LengthI(1.1, UnitsLength.REFERENCEFRAME)
        screen.linkPlate(o)
        for well_id in range(7, 9):
            well = WellI()
            well.id = rlong(well_id)
            well.column = rint(2)
            well.row = rint(1)
            well.externalDescription = \
                rstring('external_description_%d' % well_id)
            well.externalIdentifier = \
                rstring('external_identifier_%d' % well_id)
            well.type = rstring('the_type')
            well.alpha = rint(0)
            well.red = rint(255)
            well.green = rint(0)
            well.blue = rint(0)
            well.status = rstring('the_status')
            o.addWell(well)
            plateacquisition = PlateAcquisitionI()
            plateacquisition.id = rlong(well_id)
            plateacquisition.name = rstring(
                'plateacquisition_name_%d' % well_id)
            plateacquisition.description = rstring(
                'plateacquisition_description_%d' % well_id)
            plateacquisition.maximumFieldCount = rint(1)
            plateacquisition.startTime = rtime(1)
            plateacquisition.endTime = rtime(2)
            for wellsample_id in range(9, 11):
                wellsample = WellSampleI()
                wellsample.setPlateAcquisition(plateacquisition)
                wellsample.id = rlong(wellsample_id)
                wellsample.posX = LengthI(1.0, UnitsLength.REFERENCEFRAME)
                wellsample.posY = LengthI(2.0, UnitsLength.REFERENCEFRAME)
                wellsample.timepoint = rtime(1)
                wellsample.image = create_image(1)
                well.addWellSample(wellsample)

    return screen


def add_annotations(o):
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
    annotation = BooleanAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('boolean_annotation')
    annotation.boolValue = rbool(True)
    o.linkAnnotation(annotation)
    annotation = CommentAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('comment_annotation')
    annotation.textValue = rstring('text_value')
    o.linkAnnotation(annotation)
    annotation = DoubleAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('double_annotation')
    annotation.doubleValue = rdouble(1.0)
    o.linkAnnotation(annotation)
    annotation = LongAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('long_annotation')
    annotation.longValue = rlong(1)
    o.linkAnnotation(annotation)
    annotation = MapAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('map_annotation')
    annotation.setMapValue([NamedValue('a', '1'), NamedValue('b', '2')])
    o.linkAnnotation(annotation)
    annotation = TagAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('tag_annotation')
    annotation.textValue = rstring('tag_value')
    o.linkAnnotation(annotation)
    annotation = TermAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('term_annotation')
    annotation.termValue = rstring('term_value')
    o.linkAnnotation(annotation)
    annotation = TimestampAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('timestamp_annotation')
    annotation.timeValue = rtime(1)
    o.linkAnnotation(annotation)
    annotation = XmlAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('xml_annotation')
    annotation.textValue = rstring('<xml_value></xml_value>')
    o.linkAnnotation(annotation)
    annotation = FileAnnotationI()
    annotation.description = rstring('the_description')
    annotation.ns = rstring('file_annotation')
    annotation.file = OriginalFileI(1)
    annotation.file.path = rstring('path')
    annotation.file.size = rlong(2)
    annotation.file.atime = rtime(3)
    annotation.file.mtime = rtime(4)
    annotation.file.ctime = rtime(5)
    annotation.file.hash = rstring('1a0b045d')
    annotation.file.hasher = ChecksumAlgorithmI(1)
    annotation.file.hasher.value = rstring('Adler-32')
    annotation.file.mimetype = rstring('application/octet-stream')
    annotation.file.name = rstring('name')
    o.linkAnnotation(annotation)


@pytest.fixture()
def experimenter():
    o = ExperimenterI()
    o.id = rlong(1)
    o.email = rstring('the_email')
    o.firstName = rstring('the_firstName')
    o.institution = rstring('the_institution')
    o.lastName = rstring('the_lastName')
    o.middleName = rstring('the_middleName')
    o.omeName = rstring('the_omeName')
    return o


@pytest.fixture()
def experimenter_group():
    o = ExperimenterGroupI()
    o.id = rlong(1)
    o.name = rstring('the_name')
    o.description = rstring('the_description')
    return o


@pytest.fixture()
def permissions():
    o = PermissionsI()
    return o


@pytest.fixture()
def externalInfo():
    o = ExternalInfoI()
    o.entityId = rlong(123)
    o.entityType = rstring('test')
    o.lsid = rstring('ABCDEF')
    o.uuid = rstring('f90a1fd5-275c-4d14-82b3-87b5ef0f07de')
    return o


@pytest.fixture()
def permissions_cannot_link(permissions):
    permissions._restrictions = [True, False, False, False]
    return permissions


@pytest.fixture()
def permissions_cannot_edit(permissions):
    permissions._restrictions = [False, True, False, False]
    return permissions


@pytest.fixture()
def permissions_cannot_delete(permissions):
    permissions._restrictions = [False, False, True, False]
    return permissions


@pytest.fixture()
def permissions_cannot_annotate(permissions):
    permissions._restrictions = [False, False, False, True]
    return permissions


@pytest.fixture()
def details(experimenter, experimenter_group, permissions, externalInfo):
    o = DetailsI()
    o.owner = experimenter
    o.group = experimenter_group
    o.permissions = permissions
    o.externalInfo = externalInfo
    return o


@pytest.fixture()
def roi(experimenter, experimenter_group, permissions, externalInfo):
    o = RoiI()
    o.id = rlong(1)
    o.name = rstring('the_name')
    o.description = rstring('the_description')
    o.details.owner = experimenter
    o.details.group = experimenter_group
    o.details.permissions = permissions
    o.details.externalInfo = externalInfo
    return o


@pytest.fixture()
def roi_with_unloaded_details_children(roi):
    roi.details.owner = ExperimenterI(1, False)
    roi.details.group = ExperimenterGroupI(1, False)
    return roi


@pytest.fixture()
def roi_with_shapes(roi, ellipse, rectangle, point):
    roi.addShape(point)
    roi.addShape(ellipse)
    roi.addShape(rectangle)
    # Test handle of None from roi.copyShapes()
    roi.setShape(0, None)
    return roi


@pytest.fixture()
def roi_with_shapes_and_annotations(roi, ellipse, rectangle):
    roi.addShape(ellipse)
    roi.addShape(rectangle)
    add_annotations(roi)
    return roi


def populate_shape(o, transform, set_unit_attributes=True):
    o.fillColor = rint(0xffffffff)
    o.fillRule = rstring('solid')
    o.fontFamily = rstring('cursive')
    if set_unit_attributes:
        o.fontSize = LengthI(12, UnitsLength.POINT)
    o.fontStyle = rstring('italic')
    o.locked = rbool(False)
    o.strokeColor = rint(0xffff0000)
    o.strokeDashArray = rstring('inherit')
    if SCHEMA_VERSION == '2015-01':
        o.visibility = rbool(True)
        o.strokeLineCap = rstring('round')
    if set_unit_attributes:
        o.strokeWidth = LengthI(4, UnitsLength.PIXEL)
    o.textValue = rstring('the_text')
    o.theC = rint(1)
    o.theT = rint(2)
    o.theZ = rint(3)
    if SCHEMA_VERSION == '2015-01':
        o.transform = transform.svg_transform
    else:
        o.transform = transform
    return o


@pytest.fixture()
def identity_transform():
    t = AffineTransformI()
    if SCHEMA_VERSION == '2015-01':
        t.convert_svg_transform('matrix(1 0 0 1 0 0)')
    else:
        t.setA00(rdouble(1))
        t.setA10(rdouble(0))
        t.setA01(rdouble(0))
        t.setA11(rdouble(1))
        t.setA02(rdouble(0))
        t.setA12(rdouble(0))
        t.id = rlong(8)
    return t


@pytest.fixture()
def translation_transform():
    t = AffineTransformI()
    if SCHEMA_VERSION == '2015-01':
        t.convert_svg_transform('translate(3 4)')
    else:
        t.setA00(rdouble(1))
        t.setA10(rdouble(0))
        t.setA01(rdouble(0))
        t.setA11(rdouble(1))
        t.setA02(rdouble(3))
        t.setA12(rdouble(4))
        t.id = rlong(8)
    return t


@pytest.fixture()
def rotation_transform():
    t = AffineTransformI()
    if SCHEMA_VERSION == '2015-01':
        t.convert_svg_transform('rotate(45 50 100)')
    else:
        t.setA00(rdouble(0.7071067811865476))
        t.setA10(rdouble(0.7071067811865475))
        t.setA01(rdouble(-0.7071067811865475))
        t.setA11(rdouble(0.7071067811865476))
        t.setA02(rdouble(85.35533905932736))
        t.setA12(rdouble(-6.066017177982129))
        t.id = rlong(8)
    return t


@pytest.fixture()
def scale_transform():
    t = AffineTransformI()
    if SCHEMA_VERSION == '2015-01':
        t.convert_svg_transform('scale(1.5 2.5)')
    else:
        t.setA00(rdouble(1.5))
        t.setA10(rdouble(0))
        t.setA01(rdouble(0))
        t.setA11(rdouble(2.5))
        t.setA02(rdouble(0))
        t.setA12(rdouble(0))
        t.id = rlong(8)
    return t


@pytest.fixture()
def ellipse(identity_transform):
    o = EllipseI()
    populate_shape(o, identity_transform)
    if SCHEMA_VERSION == '2015-01':
        o.cx = rdouble(1.0)
        o.cy = rdouble(2.0)
        o.rx = rdouble(3.0)
        o.ry = rdouble(4.0)
    else:
        o.x = rdouble(1.0)
        o.y = rdouble(2.0)
        o.radiusX = rdouble(3.0)
        o.radiusY = rdouble(4.0)
    o.id = rlong(1)
    return o


@pytest.fixture()
def ellipse_with_annotations(ellipse):
    o = ellipse
    add_annotations(o)
    return o


@pytest.fixture()
def rectangle(identity_transform):
    o = RectangleI()
    populate_shape(o, identity_transform)
    o.x = rdouble(1.0)
    o.y = rdouble(2.0)
    o.width = rdouble(3.0)
    o.height = rdouble(4.0)
    o.id = rlong(2)
    return o


@pytest.fixture()
def point(identity_transform):
    o = PointI()
    populate_shape(o, identity_transform)
    if SCHEMA_VERSION == '2015-01':
        o.cx = rdouble(1.0)
        o.cy = rdouble(2.0)
    else:
        o.x = rdouble(1.0)
        o.y = rdouble(2.0)
    o.id = rlong(3)
    return o


@pytest.fixture()
def label(identity_transform):
    o = LabelI()
    populate_shape(o, identity_transform)
    o.x = rdouble(1.0)
    o.y = rdouble(2.0)
    o.id = rlong(7)
    return o


@pytest.fixture()
def polyline(identity_transform):
    o = PolylineI()
    populate_shape(o, identity_transform)
    o.points = rstring('0,0 1,2 3,5')
    if SCHEMA_VERSION != '2015-01':
        o.setMarkerStart('Arrow')
        o.setMarkerEnd('Arrow')
    o.id = rlong(4)
    return o


@pytest.fixture()
def polygon(identity_transform):
    o = PolygonI()
    populate_shape(o, identity_transform)
    o.points = rstring('0,0 1,2 3,5')
    o.id = rlong(5)
    return o


@pytest.fixture()
def line(identity_transform):
    o = LineI()
    populate_shape(o, identity_transform)
    o.setX1(0)
    o.setY1(0)
    o.setX2(1)
    o.setY2(2)
    if SCHEMA_VERSION != '2015-01':
        o.setMarkerStart('Arrow')
        o.setMarkerEnd('Arrow')
    o.id = rlong(6)
    return o


@pytest.fixture()
def opt_unit_label(identity_transform):
    o = LabelI()
    populate_shape(o, identity_transform, False)
    o.x = rdouble(1.0)
    o.y = rdouble(2.0)
    o.id = rlong(7)
    return o


@pytest.fixture()
def mask(identity_transform):
    o = MaskI()
    populate_shape(o, identity_transform)
    o.x = rdouble(0.0)
    o.y = rdouble(0.0)
    o.width = rdouble(1.0)
    o.height = rdouble(2.0)
    o.id = rlong(8)
    return o
