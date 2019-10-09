#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from .spcreports import spcreports
except ValueError:
    from spcreports import spcreports

try:
    from .nhcoutlooks import nhcoutlooks
except ValueError:
    from nhcoutlooks import nhcoutlooks

def get_spc_storm_reports_df(url_or_path, type_of_df = 'all'):
    '''Separates the SPC storm reports into respective hazard dataframes.
    
    Currently DOES NOT SUPPORT multiple days worth of dataframes - only one
        day at a time.
    
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

def get_nhc_past_cyclones_polygons(name, year, advisory_num):
    '''Retrieves previous cyclones from the NHC and returns geopandas dataframe
        associated with the cyclone given.
    
    Currently DOES NOT SUPPORT advisory number slicing (getting multiple
        advisories at once)
    
    Parameters
    ----------
    name: `string` (REQUIRED)
        The name of a tropical cyclone either in the Atlantic or EPAC. If the name
            does not exist, then a ValueError is thrown.
    
    year: `integer` (REQUIRED)
        The year of which the cyclone formed. If the year is not between the current
            and 2008, then it will throw a value error.
    
    advisory_num: `string` (REQUIRED)
        The advisory number of the cyclone listed under name. If it does not exist,
            then an ValueError is thrown.
    
    Returns
    -------
    `geopandas dataframe`
        The dataframe with the given parameters
    '''
    cyclone_obj = nhcoutlooks(name, year, advisory_num)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
