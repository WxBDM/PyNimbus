#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:54:31 2019

@author: Brandon
"""

from setuptools import setup

setup(
      
      name='nwstools',
      
      version='0.1',
      
      description='A Python package to grab NWS-related data',
      
      url='http://github.com/storborg/funniest',
      
      author='Brandon Molyneaux',
      
      author_email='bdmolyne@gmail.com',
      
      license='MIT',
      
      packages=['nwstools'],
      
      install_requires = ['csv', 'pandas', 'requests', 'os'],
      
      zip_safe=False,
      
      )