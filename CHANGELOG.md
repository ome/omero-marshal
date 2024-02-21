## 0.9.0 (2024-02-21)

Features:

 - Support file annotations - [#78](https://github.com/ome/omero-marshal/pull/78)
 - Add support for Python 3.11 - [#79](https://github.com/ome/omero-marshal/pull/79)

Breaking changes:

 - Drop support for Python 3.7 - [#77](https://github.com/ome/omero-marshal/pull/77)

Bugfixes:

 - Various build fixes - [#76](https://github.com/ome/omero-marshal/pull/76), [#75](https://github.com/ome/omero-marshal/pull/75), etc.

## 0.8.0 (2022-10-26)

 - Test the build of wheel. No longer test the build of egg  - [#74](https://github.com/ome/omero-marshal/pull/74)
 - Remove the usage of set-output in GitHub action - [#73](https://github.com/ome/omero-marshal/pull/73)
 
## 0.7.0 (2020-01-10)

Breaking changes:

 - Restrict omero-marshal to Python 3 only - [#66](https://github.com/ome/omero-marshal/pull/66)

Bugfixes:

 - Fix import ordering issues - [#64](https://github.com/ome/omero-marshal/pull/64)

## 0.6.3 (2019-11-06)

Bugfixes:

  - Always encode string in Decoder.set_property() [#65](https://github.com/ome/omero-marshal/pull/65)

## 0.6.2 (2019-10-25)

Bugfixes:

  - Fix relative imports on Python 3 [#63](https://github.com/ome/omero-marshal/pull/63)

## 0.6.1 (2019-08-21)

Bugfixes:

  - Use major.minor for version detection:  [#61](https://github.com/ome/omero-marshal/pull/61)

## 0.6.0 (2019-06-14)

Features:

  - Add support for OMERO 5.5 [#59](https://github.com/ome/omero-marshal/pull/59)

Bugfixes:

  - Remove support for 5.1.x [#56](https://github.com/ome/omero-marshal/pull/56)
  - Update Travis build to use Xenial and Ice 3.6.x [#53](https://github.com/ome/omero-marshal/pull/53)
  - Remove support for Python 2.6
  - Add support for Python 3

## 0.5.4 (2018-11-23)

Bugfixes:

  - Fix stringent OMERO version check [#51](https://github.com/ome/omero-marshal/pull/51)

## 0.5.3 (2018-04-17)

Bugfix:

  - Fix installation on CentOS following PyPI TLSv1.0 and TLSv1.1 deprecation [#50](https://github.com/ome/omero-marshal/pull/50)

## 0.5.2 (2017-11-06)

Features:

  - Support for Masks [#44](https://github.com/ome/omero-marshal/pull/44)

Bugfixes:

  - Test with latest OMERO 5.4.x [#43](https://github.com/ome/omero-marshal/pull/43), [#47](https://github.com/ome/omero-marhsal/pull/47)
  - Update Travis build to use Trusty and latest Ice 3.5.x [#42](https://github.com/ome/omero-marshal/pull/42)
  - Test with latest OMERO 5.3.x [#41](https://github.com/ome/omero-marshal/pull/41)

## 0.5.1 (2017-03-30)

Bugfixes:

  - Fix stringent OMERO version check [#38](https://github.com/ome/omero-marshal/pull/38)

## 0.5.0 (2017-03-13)

Features:

  - Migrate transforms encoder/decoders [#20](https://github.com/ome/omero-marshal/pull/20)
  - Support Line/Polyline markers [#25](https://github.com/ome/omero-marshal/pull/25)
  - Support Screens and Plates [#26](https://github.com/ome/omero-marshal/pull/26)
  - Support Images, Pixels and Channels [#27](https://github.com/ome/omero-marshal/pull/27), [#32](https://github.com/ome/omero-marhsal/pull/32), [#36](https://github.com/ome/omero-marhsal/pull/36)
  - Add convenience fields to encoded Permissions [#30](https://github.com/ome/omero-marshal/pull/30)
  - Support Well/WellSample/Image hierarchy [#31](https://github.com/ome/omero-marshal/pull/31)

Bugfixes:

  - Handle unloaded details [#28](https://github.com/ome/omero-marshal/pull/28)

## 0.4.1 (2016-09-16)

Bugfixes:

  - Fix null strings [#23](https://github.com/ome/omero-marshal/pull/23)

## 0.4.0 (2016-09-05)

Features:

  - Support multiple OME schemas [#12](https://github.com/ome/omero-marshal/pull/12)
  - Use _field_info while decoding [#17](https://github.com/ome/omero-marshal/pull/17)

## 0.3.1 (2016-06-22)

Features:

  - Support shape transforms [#8](https://github.com/ome/omero-marshal/pull/8)
  - Support externalinfo in details [#11](https://github.com/ome/omero-marshal/pull/11)

## 0.3.0 (2016-04-27)

Features:

  - Support both OMERO 5.1.x and 5.2.x [#2](https://github.com/ome/omero-marshal/pull/2)
  - Activate Travis for omero-marshal [#3](https://github.com/ome/omero-marshal/pull/3)

Bugfixes:

  - Fix for non existing (optional) unit type attributes [#6](https://github.com/ome/omero-marshal/pull/6)

## 0.2 (2016-02-12)

Features:

  - Support line shapes
  - Support label shapes
  - Add logging when requesting unknown encoders/decoders

## 0.1 (2015-12-04)

Initial release.
