#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:02:26 2021

@author: Tessa
"""

#census only has 5 zips on their maps
#last four digits are not attached to usable geography
#d['trim_zip'] = d['zip'].str[:5]
# new column and .str tells pandas when it's looking at the column you're about to call a str method
#left most five characters in the string
#check length of trim zip
#do what we did in class
#ditch all the zips that are not 5 or 9 and then do it

import pandas as pd

resto_loans = pd.read_pickle('resto_loans.zip')

#ditch all zips that are not 5 or 9

#trim all the zips

#remove columns not necessary
