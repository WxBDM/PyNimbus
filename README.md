# PyNimbus

[![Documentation Status](https://readthedocs.org/projects/pynimbus/badge/?version=latest)](https://pynimbus.readthedocs.io/en/latest/?badge=latest) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![Issues](https://img.shields.io/github/issues/wxbdm/PyNimbus)](https://github.com/WxBDM/PyNimbus/issues) ![Version](https://img.shields.io/pypi/v/pynimbus)

PyNimbus's goal is to take the "middle man" out of downloading and sorting data found from various National Weather Service products such as NHC and SPC outlooks. 

PyNimbus follows the [semantic version](https://semver.org/) numbering system.

## Contributing to PyNimbus
If you wish to contribute to PyNimbus, please see the [contributing file](https://github.com/WxBDM/PyNimbus/blob/master/Contributing.md).

## Asking questions about PyNimbus
If you have questions on how to use PyNimbus, please send me an email. The email can be found in the contributing file above. Please do not open an issue or pull request for questions regarding the usage of PyNimbus.

## PyNimbus Function Naming Convention

PyNimbus follows a fairly straight-forward naming convention as such: `get_<NWS BRANCH>_<PRODUCT>`. The function returns an object with various attributes such as its associated pandas data frame or polygon.

If you are unfamiliar with the various National Weather Service branches, it is worth noting the following abbreviations:

- SPC: [Storm Prediction Center](https://www.spc.noaa.gov/)

- NHC: [National Hurricane Center](https://www.nhc.noaa.gov/)

Below is a table with the current functionality. See the documentation for more information regarding these.

| Branch | Product       | Attributes               | Function Call                | Tutorial Link                                                                 |
|:------:|:-------------:|:------------------------:|:----------------------------:|:-----------------------------------------------------------------------------:|
| SPC    | Storm Reports | .df, .points             | `get_spc_storm_reports()`    | [Link](https://pynimbus.readthedocs.io/en/latest/tutorials/stormreports.html) |
| NHC    | Hurricane GIS | .polygon, .line, .points | `get_nhc_previous_cyclone()` | [Link](https://pynimbus.readthedocs.io/en/latest/tutorials/nhccyclones.html)  |

## Installing PyNimbus

The easiest way to install is through pip: `pip install pynimbus`

## License

PyNimbus falls under the BSD 3-Clause license. See the [License page](https://github.com/WxBDM/PyNimbus/blob/master/LICENSE.md) for more information.

## Important Links

- [Documentation](https://pynimbus.readthedocs.io/en/latest/)
- [Issues](https://github.com/WxBDM/PyNimbus/issues)
- [Code Repository](https://github.com/WxBDM/PyNimbus)

## Version Log

v0.1.0 - Released 10/14/19
1. PyNimbus geometries have been built. PyNimbus geometries are the building block to be able to structure and organize lat/lon pairs for easy access. 

1. `get_nhc_past_cyclone` is now here! Check out the tutorial in the PyNimbus documentation to see more about how you can use Cartopy to plot National Hurricane Center outlooks with a few lines of code!

2. PyNimbus Geometries! In essence, you can think of these as an encapsulation (and implementation) of Shapely geometries. These geometries are the foundation of all polygons, lines, and points used within PyNimbus. All geometries consist of other geometries down to a point (lat/lon pair). This is going to be needed going into the future.

