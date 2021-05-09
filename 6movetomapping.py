#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:08:52 2021

@author: Tessa
"""

#  Demonstrate using geopandas for joining data onto a shapefile. To use 
#  this script, download the Census shapefile tl_2019_us_state.zip 

import pandas as pd
import geopandas

#%%
#
#  Read the shapefile
#

states = geopandas.read_file("zip://tl_2019_us_state.zip")

print( '\nOriginal length:', len(states) )

#
#  Now filter out the states or equivalent entities that aren't part 
#  of the contiguous (or conterminous) US
#

po_notcon = ['AK','AS','GU','HI','MP','PR','VI']

is_conus = states['STUSPS'].isin(po_notcon) == False

conus = states[ is_conus ]

print( '\nFiltered length:', len(conus) )

#%%
#
#  What's in conus?
#

print( 'number of rows, columns:', conus.shape )
print( 'columns:', list(conus.columns) )