## 0.6.3 (2019-11-06)

Bugfixes:

  - Always encode string in Decoder.set_property() [#65](https://github.com/ome/omero-marhsal/pull/65)

## 0.6.2 (2019-10-25)

Bugfixes:

  - Fix relative imports on Python 3 [#63](https://github.com/ome/omero-marhsal/pull/63)

## 0.6.1 (2019-08-21)

Bugfixes:

  - Use major.minor for version detection:  [#61](https://github.com/ome/omero-marhsal/pull/61)

## 0.6.0 (2019-06-14)

Features:

  - Add support for OMERO 5.5 [#59](https://github.com/ome/omero-marhsal/pull/59)

Bugfixes:

  - Remove support for 5.1.x [#56](https://github.com/ome/omero-marhsal/pull/56)
  - Update Travis build to use Xenial and Ice 3.6.x [#53](https://github.com/ome/omero-marhsal/pull/53)
  - Remove support for Python 2.6
  - Add support for Python 3

## 0.5.4 (2018-11-23)

Bugfixes:

  - Fix stringent OMERO version check [#51](https://github.com/ome/omero-marhsal/pull/51)

## 0.5.3 (2018-04-17)

Bugfix:

  - Fix installation on CentOS following PyPI TLSv1.0 and TLSv1.1 deprecation [#50](https://github.com/ome/omero-marhsal/pull/50)

## 0.5.2 (2017-11-06)

Features:

  - Support for Masks [#44](https://github.com/ome/omero-marhsal/pull/44)

Bugfixes:

  - Test with latest OMERO 5.4.x [#43](https://github.com/ome/omero-marhsal/pull/43), [#47](https://github.com/ome/omero-marhsal/pull/47)
  - Update Travis build to use Trusty and latest Ice 3.5.x [#42](https://github.com/ome/omero-marhsal/pull/42)
  - Test with latest OMERO 5.3.x [#41](https://github.com/ome/omero-marhsal/pull/41)

## 0.5.1 (2017-03-30)

Bugfixes:

  - Fix stringent OMERO version check [#38](https://github.com/ome/omero-marhsal/pull/38)

## 0.5.0 (2017-03-13)

Features:

  - Migrate transforms encoder/decoders [#20](https://github.com/ome/omero-marhsal/pull/20)
  - Support Line/Polyline markers [#25](https://github.com/ome/omero-marhsal/pull/25)
  - Support Screens and Plates [#26](https://github.com/ome/omero-marhsal/pull/26)
  - Support Images, Pixels and Channels [#27](https://github.com/ome/omero-marhsal/pull/27), [#32](https://github.com/ome/omero-marhsal/pull/32), [#36](https://github.com/ome/omero-marhsal/pull/36)
  - Add convenience fields to encoded Permissions [#30](https://github.com/ome/omero-marhsal/pull/30)
  - Support Well/WellSample/Image hierarchy [#31](https://github.com/ome/omero-marhsal/pull/31)

Bugfixes:

  - Handle unloaded details [#28](https://github.com/ome/omero-marhsal/pull/28)

## 0.4.1 (2016-09-16)

Bugfixes:

  - Fix null strings [#23](https://github.com/ome/omero-marhsal/pull/23)

## 0.4.0 (2016-09-05)

Features:

  - Support multiple OME schemas [#12](https://github.com/ome/omero-marhsal/pull/12)
  - Use _field_info while decoding [#17](https://github.com/ome/omero-marhsal/pull/17)

## 0.3.1 (2016-06-22)

Features:

  - Support shape transforms [#8](https://github.com/ome/omero-marhsal/pull/8)
  - Support externalinfo in details [#11](https://github.com/ome/omero-marhsal/pull/11)

## 0.3.0 (2016-04-27)

Features:

  - Support both OMERO 5.1.x and 5.2.x [#2](https://github.com/ome/omero-marhsal/pull/2)
  - Activate Travis for omero-marshal [#3](https://github.com/ome/omero-marhsal/pull/3)

Bugfixes:

  - Fix for non existing (optional) unit type attributes [#6](https://github.com/ome/omero-marhsal/pull/6)

## 0.2 (2016-02-12)

Features:

  - Support line shapes
  - Support label shapes
  - Add logging when requesting unknown encoders/decoders

## 0.1 (2015-12-04)

Initial release.
