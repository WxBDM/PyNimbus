#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .nhcoutlooks import nhcoutlook
from .spcreports import spcreports

def get_spc_storm_reports(url_or_path, type_of_df = 'all'):
    '''Separates the SPC storm reports into respective hazard dataframes.
    
    Currently DOES NOT SUPPORT report day slicing (retrieving multiple days and
        adding to one dataframe).
    
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
    `object`
        An object with both the dataframe and PyNimbus Scatter Point geometry.
    '''
    return spcreports(url_or_path, type_of_df)

def get_spc_storm_reports_df(url_or_path, type_of_df = 'all', surpress_warning = False):
    '''This method is here for backwards compatability reasons. See 
    `get_spc_storm_reports()` for all the details regarding this function.'''
    # gets the dataframe and returns it.
    if not surpress_warning:
        print("This function will be depreciated in future versions." + \
              "Use get_spc_storm_reports instead.")
    
    return get_spc_storm_reports(url_or_path, type_of_df)

def get_nhc_past_cyclone(name, year, advisory_num, clean_files = True, **args):
    '''Retrieves previous cyclones from the NHC and returns geopandas dataframe
        associated with the cyclone given.
    
    Currently DOES NOT SUPPORT advisory number slicing (getting multiple
        advisories at once), as well as intermediate advisories (i.e. 24A, 12A, etc)
    
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
    `object`
        An object containing PyNimbus Polygon, Line, and Scatter Points geometries
    '''

    cyclone = nhcoutlook(name, year, advisory_num)
    cyclone.get_cyclone_outlook(**args)
    if clean_files: cyclone.clean_files()
    return cyclone    