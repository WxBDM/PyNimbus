#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:54:31 2019

@author: Brandon
"""

from setuptools import setup

setup(
      
      name='pynimbus',
      
      version='0.1',
      
      description='A Python package to organize National Weather Service product data.',
      
      url='https://github.com/WxBDM/SPC-Storm-Reports',
      
      author='Brandon Molyneaux',
      
      author_email='bdmolyne@gmail.com',
      
      license='MIT',
      
      packages=['pynimbus'],
      
      install_requires = ['pandas', 'pyshp'],
      
      zip_safe=False,
      
      )