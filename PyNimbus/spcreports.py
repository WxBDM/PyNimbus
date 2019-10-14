#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from .nimbusgeometry import ScatterPoints

class _DataFrames():

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

class _Polygons(_DataFrames):
    
    def _make_lat_lon_pairs(self):
        
        def isFloat(element):
            try:
                float(element)
                return True
            except:
                return False
        
        lats_filtered = [float(element) for element in self.df['Lat'] if isFloat(element)]
        lons_filtered = [float(element) for element in self.df['Lon'] if isFloat(element)]
        
        return list(zip(lats_filtered, lons_filtered))

    
class spcreports(_Polygons):
     
    def __init__(self, url, type_of_df):
        self._url = url
        self.df = pd.read_csv(url)
        if type_of_df != 'all':
            super()._make_dataframes_from_pandas(self.df, type_of_df.lower())
            
        self.points = ScatterPoints(super()._make_lat_lon_pairs())
    
    def __len__(self):
        return len(self.df)

    def __repr__(self):
        phrase = '''PyNimbus Storm Reports object consisting of:
    1) Pandas dataframe (attribute: df)
    2) PyNimbus Geometry Scatter Point (attribute: points)
    '''
        return phrase
        
        
