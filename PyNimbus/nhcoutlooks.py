#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:12:46 2019

@author: Brandon
"""

class nhcOutlooks():
    
    def __init__(self, name, year, advisory_num): 
        self.name = name
        self.yr = int(year)
        self.adv_n = str(advisory_num)
        
        self._check_inputs()
    
    def _import_hurricane_info():
        # return hurrs[self.yr]
        # for now, assume year is 2019.
        return {
            "Andrea"        : ["al01", "Atlantic"],
            "Barry"         : ["al02", "Atlantic"],
            "Three"         : ["al03", "Atlantic"],
            "Chantal"       : ["al04", "Atlantic"],
            "Dorian"        : ["al05", "Atlantic"],
            "Erin"          : ["al06", "Atlantic"],
            "Fernand"       : ["al07", "Atlantic"],
            "Gabrielle"     : ["al08", "Atlantic"],
            "Humberto"      : ["al09", "Atlantic"],
            "Jerry"         : ["al10", "Atlantic"],
            "Imelda"        : ["al11", "Atlantic"],
            "Karen"         : ["al12", "Atlantic"],
            "Lorenzo"       : ["al13", "Atlantic"],
            "Alvin"         : ["ep01", "East Pacific"],
            "Barbara"       : ["ep02", "East Pacific"],
            "Cosme"         : ["ep03", "East Pacific"],
            "Four-e"        : ["ep04", "East Pacific"],
            "Dalila"        : ["ep05", "East Pacific"],
            "Erick"         : ["ep06", "East Pacific"],
            "Flossie"       : ["ep07", "East Pacific"],
            "Gil"           : ["ep08", "East Pacific"],
            "Henriette"     : ["ep09", "East Pacific"],
            "Ivo"           : ["ep10", "East Pacific"],
            "Juliette"      : ["ep11", "East Pacific"],
            "Akoni"         : ["ep12", "East Pacific"],
            "Kiko"          : ["ep13", "East Pacific"],
            "Mario"         : ["ep14", "East Pacific"],
            "Lorena"        : ["ep15", "East Pacific"],
            "Narda"         : ["ep16", "East Pacific"]
            }
        # import the hurricane info; for now, hardcoded
    
    def _check_inputs(self):
        # checks to see if parameters are correct
        if not 2008 <= self.yr <= 2019:
            raise ValueError("Year must be between 2008 and current year")
        
        if self.name not in self._import_hurricane_info():
            raise ValueError("Cyclone name not in the specified year. Double check spelling and year.")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    