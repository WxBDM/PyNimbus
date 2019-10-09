#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:12:46 2019

@author: Brandon
"""

import hurricane_names as hn
import datetime

class nhcOutlooks():
    
    def __init__(self, name, year, advisory_num): 
        self._hurricane_info(name, int(year))
        
        self.name = name
        self.yr = int(year)
        self.adv_n = str(advisory_num)
    
    def _hurricane_info(self, name, year):
        
        def check_if_exists_in_dict():
            
            # put 2008 on top for forward compatability reasons - append to list below
            # for future years (2020, etc) using elif.
            if   year == 2008 : h_dict = hn.h_2008
            elif year == 2009 : h_dict = hn.h_2009
            elif year == 2010 : h_dict = hn.h_2010
            elif year == 2011 : h_dict = hn.h_2011
            elif year == 2012 : h_dict = hn.h_2012
            elif year == 2013 : h_dict = hn.h_2013
            elif year == 2014 : h_dict = hn.h_2014
            elif year == 2015 : h_dict = hn.h_2015
            elif year == 2016 : h_dict = hn.h_2016
            elif year == 2017 : h_dict = hn.h_2017
            elif year == 2018 : h_dict = hn.h_2018
            elif year == 2019 : h_dict = hn.h_2019
            
            # if the name is in the dictionary, return. If not, raise error.
            if name in h_dict:
                return h_dict[name]
            raise ValueError("{0} not in {1} - double check spelling and/or year.".format(name, year))
        
        # check to see if it's a valid year.
        now = datetime.datetime.now()
        if not 2008 <= year <= now.year:
            raise ValueError("Year must be between 2008 and current year")
        
        return check_if_exists_in_dict()
    
    
    
    
    
    
    
    
    
    
    
    