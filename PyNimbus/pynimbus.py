#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .spcreports import spcreports

def get_spc_storm_reports_df(url_or_path, type_of_df = 'all'):
    '''Separates the SPC storm reports into respective hazard dataframes.
    
    Parameters
    ----------
    url_or_path: `string` (REQUIRED)
        Either a URL or path to a storm report CSV file.
        Note: If using a URL, copy, paste, and modify YYMMDD:
            https://www.spc.noaa.gov/climo/reports/YYMMDD_rpts_filtered.csv
        Or use one of the following:
            https://www.spc.noaa.gov/climo/reports/today_filtered.csv
            https://www.spc.noaa.gov/climo/reports/yesterday_filtered.csv

    type_of_df: `string` (DEFAULT: "all")
        Either "tornado", "wind", "hail", or "all"; specifies the type of hazard
        for the dataframe.
    
    Returns
    -------
    `pandas dataframe`
        The dataframe specified with type_of_df parameter. If there are no
        reports for the specified hazard, then an empty dataframe will be returned.
    '''

    # gets the dataframe and returns it.
    reports_obj = spcreports(url_or_path, type_of_df)
    return reports_obj.df
