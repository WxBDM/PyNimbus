# Tutorial: Retrieving SPC Storm Reports
This tutorial will explain how to go about retrieving a storm report, found on the [SPC Storm Reports page](https://www.spc.noaa.gov/climo/reports/today.html).  Specifically, this tutorial explains how to use `get_spc_storm_reports_df`. This method separates the SPC storm reports into respective hazard pandas dataframes.

## Retrieving the reports
PyNimbus uses pandas to get and format the storm reports. To begin, use the `get_spc_storm_reports_df` method, as such:
```python
import pynimbus as pyn
link = "https://www.spc.noaa.gov/climo/reports/today_filtered.csv"
today_reports = pyn.get_spc_storm_reports_df(link)
```
This will return a pandas dataframe. Note that you can also use a CSV file on your machine instead of a link - simply replace `link` with the path to the associated CSV file. Note that if you opt for this, the file should not be modified.

Note that the `url_or_path` is a required argument (in the above code, it is `link`).

## Working with parameters
The only parameter in this method is `type_of_df`, which is defaulted to `all`. There are only 4 possible inputs for this parameter: `all`, `tornado`, `wind`, and `hail`. Depending upon the input, it will return the dataframe pertaining to the hazard. For example:
```python
import pynimbus as pyn
link = "https://www.spc.noaa.gov/climo/reports/160524_rpts_filtered.csv"
ddc_reports = pyn.get_spc_storm_reports_df(link, type_of_df = 'tornado')
```
will return the dataframe with just tornado reports. Likewise, if you were to change it to `type_of_df = 'wind'`, it would return a dataframe with only wind reports from this day.  

### But what if I want to save the dataframe to a CSV file?
Pandas has your back on this one:
```python
import pandas as pd
import pynimbus as pyn
link =  "https://www.spc.noaa.gov/climo/reports/160524_rpts_filtered.csv"
df = pyn.get_spc_storm_reports_df(link, type_of_df = 'tornado')
df.to_csv("/path/to/save/csv", *args)
```
It was decided to not integrate this directly into the method, as this method is easier to work with.

## Additional resources
- Pandas 0.25.0 documentation ([link](https://pandas.pydata.org/pandas-docs/stable/))
- GitHub project repository ([link](https://github.com/WxBDM/PyNimbus))
