#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:34:24 2019

@author: Brandon
"""

class StormReportsChecks:
    
    def __init__(self):
        pass
    
    def check_storm_reports_df_type(self, inp):
        '''Checks the input of the storm report input under nwstools.py'''
        if inp.lower() not in ['all', 'tornado', 'wind', 'hail']:
            phrase = 'type_of_df must either be tornado, wind, hail, all, or object.'
            raise ValueError(phrase)
    
    def check_save_file_info(self, csv, path):
        if csv: # csv file is being saved. Check path
            if type(path) is None:
                phrase = 'path_to_save_csv must be a path on your machine'
                raise ValueError(phrase)
        
            