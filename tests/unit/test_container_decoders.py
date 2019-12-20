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

from omero_marshal import get_encoder, get_decoder
from omero.model import LengthI
from omero.rtypes import rint
from omero.model.enums import UnitsLength
import pytest


class TestProjectDecoder(object):

    def assert_project(self, project):
        assert project.name.val == 'the_name'
        assert project.description.val == 'the_description'

    def test_project_decoder(self, project):
        encoder = get_encoder(project.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project)
        v = decoder.decode(v)
        self.assert_project(v)
        assert v.sizeOfDatasetLinks() == 0

    def test_project_with_datasets_decoder(self, project_with_datasets):
        encoder = get_encoder(project_with_datasets.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project_with_datasets)
        v = decoder.decode(v)
        assert v.id.val == 1
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfDatasetLinks() == 2
        dataset_1, dataset_2 = v.linkedDatasetList()
        assert dataset_1.id.val == 1
        assert dataset_1.name.val == 'dataset_name_1'
        assert dataset_1.description.val == 'dataset_description_1'
        assert dataset_2.id.val == 2
        assert dataset_2.name.val == 'dataset_name_2'
        assert dataset_2.description.val == 'dataset_description_2'

    def test_project_with_datasets_and_images_decoder(
            self, project_with_datasets_and_images):
        encoder = get_encoder(project_with_datasets_and_images.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project_with_datasets_and_images)
        v = decoder.decode(v)
        assert v.id.val == 1
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfDatasetLinks() == 2

        dataset_1, dataset_2 = v.linkedDatasetList()

        assert dataset_1.id.val == 1
        assert dataset_1.name.val == 'dataset_name_1'
        assert dataset_1.description.val == 'dataset_description_1'
        image_1, image_2 = dataset_1.linkedImageList()
        assert image_1.id.val == 1
        assert image_1.acquisitionDate.val == 1
        assert image_1.archived.val is False
        assert image_1.description.val == 'image_description_1'
        assert image_1.name.val == 'image_name_1'
        assert image_1.partial.val is False
        assert image_1.format.id.val == 1
        assert image_1.format.value.val == 'PNG'
        assert image_2.id.val == 2
        assert image_2.acquisitionDate.val == 1
        assert image_2.archived.val is False
        assert image_2.description.val == 'image_description_2'
        assert image_2.name.val == 'image_name_2'
        assert image_2.partial.val is False
        assert image_2.format.id.val == 1
        assert image_2.format.value.val == 'PNG'

        assert dataset_2.id.val == 2
        assert dataset_2.name.val == 'dataset_name_2'
        assert dataset_2.description.val == 'dataset_description_2'
        image_3, image_4 = dataset_2.linkedImageList()
        assert image_3.id.val == 3
        assert image_3.acquisitionDate.val == 1
        assert image_3.archived.val is False
        assert image_3.description.val == 'image_description_3'
        assert image_3.name.val == 'image_name_3'
        assert image_3.partial.val is False
        assert image_3.format.id.val == 1
        assert image_3.format.value.val == 'PNG'
        assert image_4.id.val == 4
        assert image_4.acquisitionDate.val == 1
        assert image_4.archived.val is False
        assert image_4.description.val == 'image_description_4'
        assert image_4.name.val == 'image_name_4'
        assert image_4.partial.val is False
        assert image_4.format.id.val == 1
        assert image_4.format.value.val == 'PNG'


class TestScreenDecoder(object):

    def assert_screen(self, screen):
        assert screen.name.val == 'the_name'
        assert screen.description.val == 'the_description'
        assert screen.protocolDescription.val == 'the_protocol_description'
        assert screen.protocolIdentifier.val == 'the_protocol_identifier'
        assert screen.reagentSetDescription.val == \
            'the_reagent_set_description'
        assert screen.reagentSetDescription.val == \
            'the_reagent_set_description'
        assert screen.reagentSetIdentifier.val == 'the_reagent_set_identifier'
        assert screen.type.val == 'the_type'

    def assert_plate(self, plate, plate_id):
        assert plate.id.val == plate_id
        assert plate.name.val == 'plate_name_%d' % plate_id
        assert plate.description.val == 'plate_description_%d' % plate_id
        assert plate.columnNamingConvention.val == 'number'
        assert plate.rowNamingConvention.val == 'letter'
        assert plate.columns.val == 12
        assert plate.rows.val == 8
        assert plate.defaultSample.val == 0
        assert plate.externalIdentifier.val == \
            'external_identifier_%d' % plate_id
        assert plate.status.val == 'status_%d' % plate_id
        assert plate.wellOriginX.__class__ is LengthI
        assert plate.wellOriginX.getUnit() == UnitsLength.REFERENCEFRAME
        assert plate.wellOriginX.getValue() == 0.1
        assert plate.wellOriginY.__class__ is LengthI
        assert plate.wellOriginY.getUnit() == UnitsLength.REFERENCEFRAME
        assert plate.wellOriginY.getValue() == 1.1

        well_1, well_2 = plate.copyWells()

        assert well_1.id.val == 7
        assert well_1.column.val == 2
        assert well_1.row.val == 1
        assert well_1.externalDescription.val == 'external_description_7'
        assert well_1.externalIdentifier.val == 'external_identifier_7'
        assert well_1.type.val == 'the_type'
        assert well_1.alpha.val == 0
        assert well_1.red.val == 255
        assert well_1.green.val == 0
        assert well_1.blue.val == 0
        assert well_1.status.val == 'the_status'
        wellsample_1, wellsample_2 = well_1.copyWellSamples()
        assert wellsample_1.posX.__class__ is LengthI
        assert wellsample_1.posX.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_1.posX.getValue() == 1.0
        assert wellsample_1.posY.__class__ is LengthI
        assert wellsample_1.posY.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_1.posY.getValue() == 2.0
        assert wellsample_1.timepoint.val == 1
        assert wellsample_1.image is not None
        assert wellsample_2.posX.__class__ is LengthI
        assert wellsample_2.posX.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_2.posX.getValue() == 1.0
        assert wellsample_2.posY.__class__ is LengthI
        assert wellsample_2.posY.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_2.posY.getValue() == 2.0
        assert wellsample_2.timepoint.val == 1
        assert wellsample_2.image is not None
        plateacquisition_1 = wellsample_1.getPlateAcquisition()
        plateacquisition_2 = wellsample_2.getPlateAcquisition()
        assert plateacquisition_1.name.val == 'plateacquisition_name_%d' % 7
        assert (plateacquisition_1.description.val ==
                'plateacquisition_description_%d' % 7)
        assert plateacquisition_1.maximumFieldCount.val == 1
        assert plateacquisition_1.startTime.val == 1
        assert plateacquisition_1.endTime.val == 2
        assert plateacquisition_2.name.val == 'plateacquisition_name_%d' % 7
        assert (plateacquisition_2.description.val ==
                'plateacquisition_description_%d' % 7)
        assert plateacquisition_2.maximumFieldCount.val == 1
        assert plateacquisition_2.startTime.val == 1
        assert plateacquisition_2.endTime.val == 2
        assert well_2.id.val == 8
        assert well_2.column.val == 2
        assert well_2.row.val == 1
        assert well_2.externalDescription.val == 'external_description_8'
        assert well_2.externalIdentifier.val == 'external_identifier_8'
        assert well_2.type.val == 'the_type'
        assert well_2.alpha.val == 0
        assert well_2.red.val == 255
        assert well_2.green.val == 0
        assert well_2.blue.val == 0
        assert well_2.status.val == 'the_status'
        wellsample_1, wellsample_2 = well_2.copyWellSamples()
        assert wellsample_1.posX.__class__ is LengthI
        assert wellsample_1.posX.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_1.posX.getValue() == 1.0
        assert wellsample_1.posY.__class__ is LengthI
        assert wellsample_1.posY.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_1.posY.getValue() == 2.0
        assert wellsample_1.timepoint.val == 1
        assert wellsample_1.image is not None
        assert wellsample_2.posX.__class__ is LengthI
        assert wellsample_2.posX.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_2.posX.getValue() == 1.0
        assert wellsample_2.posY.__class__ is LengthI
        assert wellsample_2.posY.getUnit() == UnitsLength.REFERENCEFRAME
        assert wellsample_2.posY.getValue() == 2.0
        assert wellsample_2.timepoint.val == 1
        assert wellsample_2.image is not None
        plateacquisition_1 = wellsample_1.getPlateAcquisition()
        plateacquisition_2 = wellsample_2.getPlateAcquisition()
        assert plateacquisition_1.name.val == 'plateacquisition_name_%d' % 8
        assert (plateacquisition_1.description.val ==
                'plateacquisition_description_%d' % 8)
        assert plateacquisition_1.maximumFieldCount.val == 1
        assert plateacquisition_1.startTime.val == 1
        assert plateacquisition_1.endTime.val == 2
        assert plateacquisition_2.name.val == 'plateacquisition_name_%d' % 8
        assert (plateacquisition_2.description.val ==
                'plateacquisition_description_%d' % 8)
        assert plateacquisition_2.maximumFieldCount.val == 1
        assert plateacquisition_2.startTime.val == 1
        assert plateacquisition_2.endTime.val == 2

    def test_screen_decoder(self, screen):
        encoder = get_encoder(screen.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(screen)
        v = decoder.decode(v)
        self.assert_screen(v)
        assert v.sizeOfPlateLinks() == 0

    def test_screen_with_plates_decoder(self, screen_with_plates):
        encoder = get_encoder(screen_with_plates.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(screen_with_plates)
        v = decoder.decode(v)
        self.assert_screen(v)
        assert v.id.val == 4
        assert v.sizeOfPlateLinks() == 2
        plate_1, plate_2 = v.linkedPlateList()
        self.assert_plate(plate_1, 5)
        self.assert_plate(plate_2, 6)

    @pytest.mark.parametrize("color", [
        (255, 0, 0, 255, -16776961),     # Red
        (0, 255, 0, 255, 16711935),      # Green
        (0, 0, 255, 255, 65535),         # Blue
        (0, 255, 255, 255, 16777215),    # Cyan
        (255, 0, 255, 255, -16711681),   # Magenta
        (255, 255, 0, 255, -65281),      # Yellow
        (0, 0, 0, 255, 255),             # Black
        (255, 255, 255, 255, -1),        # White
        (0, 0, 0, 127, 127),             # Transparent black
        (127, 127, 127, 127, 2139062143),  # Grey
        (255, 0, 0, None, -16776961),    # Red (no alpha)
        (None, 0, 0, None, None),        # red None
        (None, None, None, None, None)])  # None
    def test_well_color_decoder(self, color, well):
        """Test different combinations of r, g, b, a."""
        well.red = rint(color[0])
        well.green = rint(color[1])
        well.blue = rint(color[2])
        well.alpha = rint(color[3])
        encoder = get_encoder(well.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(well)
        # Check we get the expected Integer
        assert v.get('Color') == color[4]
        v = decoder.decode(v)
        # If red is None, all are None
        if color[0] is None:
            assert v.red is None
            assert v.green is None
            assert v.blue is None
            assert v.alpha is None
        elif color[3] is None:
            # alpha None -> 255 by default
            assert v.red.val == color[0]
            assert v.green.val == color[1]
            assert v.blue.val == color[2]
            assert v.alpha.val == 255
        else:
            # Otherwise, all preserved
            assert v.red.val == color[0]
            assert v.green.val == color[1]
            assert v.blue.val == color[2]
            assert v.alpha.val == color[3]
