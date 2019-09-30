#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
try:
    from .connections import connections
except ValueError:
    from connections import connections

class spcreports(connections):
    
    def __init__(self, url, type_of_df):
        
        self._url = url
        self.df = pd.read_csv(url)
        if type_of_df != 'all':
            self._make_dataframes_from_pandas(self.df, type_of_df.lower())

    def _make_dataframes_from_pandas(self, df, type_df):
        '''makes the dataframes from pandas reading in csv file (or url)'''
        # grabs the index where the next report begins
        findIndex = self.df['Time'].tolist()
        index = [i for i in range(len(findIndex)) if findIndex[i] == 'Time']
        
        # general logic:
        #   1. Split report based upon hazard; done thorugh df.drop()
        #   2. If needed, swap out headers to reflect hazard properly.
        
        # split report based upon hazard.
        if type_df == 'tornado':
            self.df = self.df.drop(index = range(index[0], len(self.df)))
            return 
        elif type_df == 'wind':
            self.df = self.df.drop(index = range(0, index[0]))
            self.df = self.df.drop(index = range(index[1], len(self.df)))
        else: # for hail
            self.df = self.df.drop(index = range(0, index[1]))
        
        self._rename_columns()
    
    def _rename_columns(self):
        newCols = self.df.iloc[0].tolist()
        self.df = self.df.reset_index()
        self.df = self.df.drop(columns = 'index')
        self.df = self.df.drop(index = 0)
        
        # dictionary to rename
        d = {}
        for i, oldName in enumerate(list(self.df)):
            d[oldName] = newCols[i]
        
        self.df = self.df.rename(columns = d)
    
    def _set_meta(self):
        '''Sets the metadata - used 
        to check if a connection has been established'''
        #Note: If using a URL, copy, paste, and modify YYMMDD:
        #    https://www.spc.noaa.gov/climo/reports/YYMMDD_rpts_filtered.csv
        #Or use one of the following:
        #    https://www.spc.noaa.gov/climo/reports/today_filtered.csv
        #    https://www.spc.noaa.gov/climo/reports/yesterday_filtered.csv
        
        # Metadata includes the day of the report. If it's "today", get
        #   the current date. If it's "yesterday", get yesterday's date.
        
        # the variable to identify "today", "yesterday" or "YYMMDD"
        which = self._url.split("/")[-1]
        which = which.split("_")[0]
        
        # handle the YYMMDD
        self.date = int(which)
        
        
        
        
        
        
        
        
        
