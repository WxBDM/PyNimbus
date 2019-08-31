# Tutorial: Retrieving SPC Storm Reports

This tutorial will explain how to go about retrieving a storm report, found on the [SPC Storm Reports page](https://www.spc.noaa.gov/climo/reports/today.html).  Specifically, this tutorial explains how to use `get_spc_storm_reports_df`. 

## Summary

This method separates the SPC storm reports into respective hazard pandas dataframes in one line of code. When called, it will return a pandas dataframe with the associated hazards.

Required argument: `url_or_path` (string)- The URL to the storm reports CSV *or* path to CSV

Optional argument: `type_of_df` (string)- The type of pandas dataframe to be returned; either all, tornado, wind, or hail. Default: all

## Retrieving the reports

PyNimbus uses pandas to get and format the storm reports. To begin, use the `get_spc_storm_reports_df` method, as such:

```python
import pynimbus as pyn
link = "https://www.spc.noaa.gov/climo/reports/today_filtered.csv"
today_reports = pyn.get_spc_storm_reports_df(link)
```

This will return a pandas dataframe with all 3 hazards: tornado, wind, and hail (as this is the default value; more on this later). Note that you can also use a CSV file located your machine instead of a link - simply replace the `link` variable with the path to the associated CSV file. If you opt for this, the associated file should not be modified in terms of columns (i.e. adding and removing columns).  

Also note that the `url_or_path` is a required argument (in the above example, the parameter being passed in is `link`).  

## Working with parameters

Suppose you wanted to retrieve all of reports from 5/24/2016; simply change the link to the CSV file:

```python
import pynimbus as pyn
link = "https://www.spc.noaa.gov/climo/reports/160524_rpts_filtered.csv"
ddc_reports = pyn.get_spc_storm_reports_df(link)
```

But now suppose you only want the tornado reports:  

```python
import pynimbus as pyn
link = "https://www.spc.noaa.gov/climo/reports/160524_rpts_filtered.csv"
ddc_reports = pyn.get_spc_storm_reports_df(link, type_of_df = 'tornado')
```

Likewise, with wind or hail, you would change the `type_of_df` parameter to either `wind` or `hail`.

### Working with the link to retrieve a certain day

"Today" storm reports: `"https://www.spc.noaa.gov/climo/reports/today_filtered.csv"`  
"Yesterday" storm reports:  `"https://www.spc.noaa.gov/climo/reports/yesterday_filtered.csv"`  
YYMMDD storm reports: `"https://www.spc.noaa.gov/climo/reports/YYMMDD_rpts_filtered.csv"`  

### But what if I want to save the dataframe to a CSV file?

Simply call the pandas `to_csv` method:  

```python
import pandas as pd
import pynimbus as pyn
link = "https://www.spc.noaa.gov/climo/reports/160524_rpts_filtered.csv"
df = pyn.get_spc_storm_reports_df(link, type_of_df = 'tornado')
df.to_csv("/path/to/save/csv")
```

It was decided to not integrate this directly into PyNimbus, as the above is easier on the user-end. However, a future version may have integration.  

## Additional resources

- Pandas 0.25.0 documentation ([link](https://pandas.pydata.org/pandas-docs/stable/))
- PyNimbus GitHub repository ([link](https://github.com/WxBDM/PyNimbus))

Last updated: 8/31/19, v0.1.0
