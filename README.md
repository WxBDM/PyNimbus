# PyNimbus

[![Documentation Status](https://readthedocs.org/projects/pynimbus/badge/?version=latest)](https://pynimbus.readthedocs.io/en/latest/?badge=latest) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![Issues](https://img.shields.io/github/issues/wxbdm/PyNimbus)](https://github.com/WxBDM/PyNimbus/issues) ![Version](https://img.shields.io/pypi/v/pynimbus)

PyNimbus's goal is to take the "middle man" out of downloading and sorting data found from various National Weather Service products such as NHC and SPC outlooks. 

PyNimbus follows the [semantic version](https://semver.org/) numbering system.

## PyNimbus Function Naming Convention

PyNimbus follows a fairly straight-forward naming convention. Here is how it is mapped out: `get_<NWS BRANCH>_<PRODUCT>_<DATA TYPE>`.

For example, if you wanted to obtain the SPC storm reports as a dataframe, the function name would be `get_spc_storm_reports_df`.

If you are unfamiliar with the various National Weather Service branches, it is worth noting the following abbreviations:

- SPC: [Storm Prediction Center](https://www.spc.noaa.gov/)

- NHC: [National Hurricane Center](https://www.nhc.noaa.gov/)

Below is a table with the (current) API functions. See the documentation for more information regarding these.

| Branch | Product       | Return Type      | Method name                  | Tutorial Link                                                                 |
|:------:|:-------------:|:----------------:|:----------------------------:|:-----------------------------------------------------------------------------:|
| SPC    | Storm Reports | pandas dataframe | `get_spc_storm_reports_df()` | [Link](https://pynimbus.readthedocs.io/en/latest/tutorials/stormreports.html) |

Future implementations include:

- Categorial and Probabilistic outlooks from SPC

- Previous hurricane information from NHC

- NHC outlooks

## Installing PyNimbus

The easiest way to install is through pip: `pip install pynimbus`

Note that the only requires pandas >= 0.23.2

## License

PyNimbus falls under the BSD 3-Clause license. See the [License page]([https://github.com/WxBDM/PyNimbus/blob/master/LICENSE.md](https://github.com/WxBDM/PyNimbus/blob/master/LICENSE.md) for more information.

## Important Links

- [Documentation](https://pynimbus.readthedocs.io/en/latest/)
- [Issues](https://github.com/WxBDM/PyNimbus/issues)
- [Code Repository](https://github.com/WxBDM/PyNimbus)
