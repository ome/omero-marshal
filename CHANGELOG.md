## 0.6.0 (2018-12-)

Bugfixes:
  - Remove support for 5.1.x (#56)
  - Update Travis build to use Xenial and Ice 3.6.x (#53)
  - Remove support for Python 2.6
  - Add support for Python 3

## 0.5.4 (2018-11-23)

Bugfixes:

  - Fix stringent OMERO version check (#51)

## 0.5.3 (2018-04-17)

Bugfix:

  - Fix installation on CentOS following PyPI TLSv1.0 and TLSv1.1 deprecation (#50)

## 0.5.2 (2017-11-06)

Features:

  - Support for Masks (#44)

Bugfixes:

  - Test with latest OMERO 5.4.x (#43, #47)
  - Update Travis build to use Trusty and latest Ice 3.5.x (#42)
  - Test with latest OMERO 5.3.x (#41)

## 0.5.1 (2017-03-30)

Bugfixes:

  - Fix stringent OMERO version check (#38)

## 0.5.0 (2017-03-13)

Features:

  - Migrate transforms encoder/decoders (#20)
  - Support Line/Polyline markers (#25)
  - Support Screens and Plates(#26)
  - Support Images, Pixels and Channels (#27, #32, #36)
  - Add convenience fields to encoded Permissions (#30)
  - Support Well/WellSample/Image hierarchy (#31)

Bugfixes:

  - Handle unloaded details (#28)

## 0.4.1 (2016-09-16)

Bugfixes:

  - Fix null strings (#23)

## 0.4.0 (2016-09-05)

Features:

  - Support multiple OME schemas (#12)
  - Use _field_info while decoding (#17)

## 0.3.1 (2016-06-22)

Features:

  - Support shape transforms (#8)
  - Support externalinfo in details (#11)

## 0.3.0 (2016-04-27)

Features:

  - Support both OMERO 5.1.x and 5.2.x (#2)
  - Activate Travis for omero-marshal (#3)

Bugfixes:

  - Fix for non existing (optional) unit type attributes (#6)

## 0.2 (2016-02-12)

Features:

  - Support line shapes
  - Support label shapes
  - Add logging when requesting unknown encoders/decoders

## 0.1 (2015-12-04)

Initial release.
