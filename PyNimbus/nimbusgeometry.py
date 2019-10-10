#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:27:29 2019

@author: Brandon
"""

import math
from shapely.geometry import Polygon, LineString, Point, MultiPoint

# This class encapsulates shapely geometries that is integrated with PyNimbus.
class PyNimbus_Geometry(object):
    '''All polygons that are created using PyNimbus implement a lot of the features
    from the Shapely library. However, not all are needed and there are some methods
    that are useful for PyNimbus's purposes.
    
    For a full list of the shapely library, visit the documentation:
        https://shapely.readthedocs.io/en/stable/manual.html
        
    All geometries are in lat/lon coordinates'''
    
    
    def set_attributes(self, pynimbus_geometry):
        self.area = pynimbus_geometry.area       # area
        self.bounds = pynimbus_geometry.bounds   # min/max of upper/lower/left/right
        self._geometry = pynimbus_geometry       # needed for below methods
        self.display = pynimbus_geometry         # this is for UI purposes
        self.coords = self._get_coordinates()   # coordinates of geometry
        self.center = pynimbus_geometry.centroid # center of geometry
        
    def _get_coordinates(self):
        return list(self._geometry.__geo_interface__['coordinates'][0])
     
    def find_distance_to(self, other):
        '''Finds the distance between two PyNimbus geometries using the
        Haversine formula between two points.
        
        Note that this only calculates the distance between two NimbusPoints.
        NimbusLines and NimbusPolygons shouldn't be used. Unexpected results
        may occur (and likely will).
        
        Parameters
        ----------
        other: `nhcoutlook.PyNimbus_Geometry`

        Returns
        -------
        distance: `float`
            Units: kilometers
        '''
    
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(math.radians, [self.lon, other.lon, self.lat, other.lat])
    
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        r = 6371 # Radius of earth in kilometers
        return c * r
    
    def contains(self, other):
        '''Determines if a PyNimbus geometry contains another geometry
        Parameters
        ----------
        other: `nhcoutlook.PyNimbus_Geometry`

        Returns
        -------
        boolean: `boolean`
        '''
        return self._geometry.contains(other._geometry)
    
    def crosses(self, other):
        '''Determines if 2 PyNimbus geometries cross eachother.
        Parameters
        ----------
        other: `nhcoutlook.PyNimbus_Geometry`

        Returns
        -------
        boolean: `boolean`
        '''
        return self._geometry.crosses(other._geometry)
    
    def is_disjointed_from(self, other):
        '''Determines if 2 PyNimbus geometries are disjointed
        Parameters
        ----------
        other: `nhcoutlook.PyNimbus_Geometry`

        Returns
        -------
        boolean: `boolean`
        '''
        return self._geometry.disjoint(other._geometry)
    
    def intersects_with(self, other):
        '''Determines if 2 geometries intersect eachother.
        Parameters
        ----------
        other: `nhcoutlook.PyNimbus_Geometry`

        Returns
        -------
        boolean: `boolean`
        '''
        return self._geometry.intersects(other._geometry)


class DataChecks():
    
    def check_point_type(self, pair):
        
        # data STRUCTURE checking
        # if it's a list, convert to tuple
        if type(pair) is list:
            pair = tuple(pair)
        # if it's anything else but a tuple, raise error.
        if type(pair) is not tuple:
            raise TypeError("Lat/Lon pairs must be a tuple.")
        
        # length checking
        if len(pair) != 2:
            raise TypeError("Lat/Lon pairs need to be length of 2.")
            
        # data TYPE checking
        type_pairs = [pair[0], pair[1]]
        for i in [0, 1]:
            # if it's an int, change to float
            if type(type_pairs[i]) is int:
                type_pairs[i] = float(type_pairs[i])
            # if it's anything else but a float, raise error.
            if type(type_pairs[i]) is not float:
                raise TypeError("Ensure all pairs of lats/lons are ints or floats.")
            
        # Check if lat/lon falls within the proper range(s)
        # latitude: -90 to 90 inclusive
        # longitude: -180 to 180 inclusive
        if type_pairs[0] < -90.0  or type_pairs[0] > 90.0:
            raise TypeError("Latitude value must be -90 <= lat <= 90")
        if type_pairs[1] < -180 or type_pairs[0] > 180:
            raise TypeError("Longitude value must be -180 <= lon <= 180")
        
        return tuple(type_pairs)
    
    def check_polygon_or_line_type(self, collection):
        
        # Check steps:
        # 1. If the outer structure is a list
        # 2. If there's at least 3 elements
        # 3. If all elements are a tuple (simply call check_point_type)
        
        # Step 1
        if type(collection) != list:
            phrase = '''Collection must be a list. For example:
    collection = [(9, 10), (2, 4), (3, 1), ...] where tuples are lat/lon pairs'''
            raise TypeError(phrase)
        
        # Step 2
        if len(collection) < 3:
            raise ValueError("Polygon must contain at least 3 lat/lon pairs")
        
        # Step 3
        # using enumerate here because there's a possibility that the tuple
        #   needs to get replaced; also allows to get the length
        for index, element in enumerate(collection):
            pair = self.check_point_type(element)
            collection[index] = pair
        
        return [collection, len(collection)]
            
            
class NimbusPoint(DataChecks, PyNimbus_Geometry):
    # This class creates a NimbusPoint - shapely.
    def __init__(self, lat_lon_pair):
        _pair = super().check_point_type(lat_lon_pair) # Data Checks
        self._point = Point(_pair) # create the point using shapely
        
        # sets lat and lon of point.
        self.lat = self._point.__geo_interface__['coordinates'][0]
        self.lon = self._point.__geo_interface__['coordinates'][1]
        super().set_attributes(self._point) # Sets rest of attributes; see PyNimbus_Geometry
    
    def __len__(self):
        return 2
    
    def __repr__(self):
        return self.get_coordinates()
    
    def get_coordinates(self):
        # Returns a tuple containing (lat, lon) pair.
        return(tuple(self.lat, self.lon))


class NimbusPolygon(DataChecks, PyNimbus_Geometry):
    # this class creates a NimbusPolygon - Shapely Polygon
    def __init__(self, lat_lon_pair_list):
        # collection returns the "corrected" collection and the length of it.
        self.__collection = super().check_polygon_or_line_type(lat_lon_pair_list)
        self._polygon = Polygon(self.__collection[0]) # the shapely polygon
        super().set_attributes(self._polygon) # sets remainder attributes
    
    def __len__(self):
        return self.__collection[1]
    
    def __repr__(self):
        return self.__polygon

    def lats_to_list(self):
        return [coord[0] for coord in self.iterable_pairs_coords()]

    def lons_to_list(self):
        return [coord[1] for coord in self.iterable_pairs_coords()]
    
    def iterable_pairs_coords(self):
        return self.coords
    
class NimbusLine(DataChecks, PyNimbus_Geometry):
    # this class creates a NimbusLine - Shapely Line
    def __init__(self, lat_lon_pair_list):
        self.__collection = super().check_polygon_or_line_type(lat_lon_pair_list)
        self._polygon = LineString(self.__collection[0]) # the shapely polygon
        super().set_attributes(self._polygon) # sets remainder attributes
    
    def get_line(self):
        pass











