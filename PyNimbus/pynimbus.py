#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from .spcreports import spcreports
except ValueError:
    from spcreports import spcreports

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

def get_nhc_past_cyclones_df(name, year, advisory_num):
    '''Retrieves previous cyclones from the NHC and returns geopandas dataframe
        associated with the cyclone given.
    
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
    
    # checks to see if parameters are correct
    if not 2008 <= year <= 2019:
        raise ValueError("Year must be between 2008 and current year")
    
    # factor into a different file once merge request is finished
    h_2019 = {"Andrea" : ["al01", "Atlantic"],
            "Barry" :  ["al02", "Atlantic"],
            "Three" : ["al03", "Atlantic"],
            "Chantal" : ["al04", "Atlantic"],
            "Dorian" : ["al05", "Atlantic"],
            "Erin" : ["al06", "Atlantic"],
            "Fernand" : ["al07", "Atlantic"],
            "Gabrielle" : ["al08", "Atlantic"],
            "Humberto" : ["al09", "Atlantic"],
            "Jerry" : ["al10", "Atlantic"],
            "Imelda" : ["al11", "Atlantic"],
            "Karen" : ["al12", "Atlantic"],
            "Lorenzo" : ["al13", "Atlantic"],
            "Alvin" : ["ep01", "East Pacific"],
            "Barbara" : ["ep02", "East Pacific"],
            "Cosme" : ["ep03", "East Pacific"],
            "Four-e" : ["ep04", "East Pacific"],
            "Dalila" : ["ep05", "East Pacific"],
            "Erick" : ["ep06", "East Pacific"],
            "Flossie" : ["ep07", "East Pacific"],
            "Gil" : ["ep08", "East Pacific"],
            "Henriette" : ["ep09", "East Pacific"],
            "Ivo" : ["ep10", "East Pacific"],
            "Juliette" : ["ep11", "East Pacific"],
            "Akoni" : ["ep12", "East Pacific"],
            "Kiko" : ["ep13", "East Pacific"],
            "Mario" : ["ep14", "East Pacific"],
            "Lorena" : ["ep15", "East Pacific"],
            "Narda" : ["ep16", "East Pacific"],
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
