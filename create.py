#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:54:40 2021

@author: Tessa
"""

#In this script I will take the Payroll Protection Program (PPP) 
#loans Freedom of Information Act (FOIA) files into one dataframe for 
#further use in the analysis.

import pandas as pd

#Create a data frame with each CSV file. This data is from May 2, 2021, 9:30 PM (UTC-04:00)
#It can be downloaded at https://data.sba.gov/dataset/ppp-foia 
#All 12 avaiable CSV files will be used

loan1=pd.read_csv('public_up_to_150k_1.csv', dtype=str)

loan2=pd.read_csv('public_up_to_150k_2.csv', dtype=str)

loan3=pd.read_csv('public_up_to_150k_3.csv', dtype=str)

loan4=pd.read_csv('public_up_to_150k_4.csv', dtype=str)

loan5=pd.read_csv('public_up_to_150k_5.csv', dtype=str)

loan6=pd.read_csv('public_up_to_150k_6.csv', dtype=str)

loan7=pd.read_csv('public_up_to_150k_7.csv', dtype=str)

loan8=pd.read_csv('public_up_to_150k_8.csv', dtype=str)

loan9=pd.read_csv('public_up_to_150k_9.csv', dtype=str)

loan10=pd.read_csv('public_up_to_150k_10.csv', dtype=str)

loan11=pd.read_csv('public_up_to_150k_11.csv', dtype=str)

loan12=pd.read_csv('public_150k_plus.csv', dtype=str)

#Compile into one dataframe

allloans=loan1.append([loan2, loan3, loan4, loan4, loan5, loan6, loan7, loan8, loan9, loan10, loan11, loan12])

#Now from all the all the loans I will find the businesses that correspond to restaurant or reaturant adjacent businesses
#NAICS codes are sourced from here https://www.census.gov/eos/www/naics/reference_files_tools/1997/sec72.htm#:~:text=722110%20Full%2DService%20Restaurants,service)%20and%20pay%20after%20eating.

resto_naics_dict={"722110": "Full-Service Restaurants",
             "722211": "Limited-Service Resturants",
             "722212": "Cafeterias",
             "722213": "Snack and Nonalcoholic Beverage Bars",
             "722310": "Food Service Contractors",
             "722320": "Caterers",
             "722330":" Mobile Food Services",
             "722410": "Drinking Places (Alcoholic Beverages)"}

resto_naics_list=["722110", "722211", "722212","722213","722310","722320", "722330", "722410"]

is_res = allloans['NAICSCode'].isin(["722110", "722211", "722212", "722213", "722310", "722320", "722330", "722410"])   

resto_loans = allloans[is_res]    

resto_loans.to_pickle('resto_loans.zip')

index=resto_loans.index
number_rows=len(index)
print("After combining all the FOIA PPP data and sorting it based upon NAICS codes, the number of PPP loans for restaurants is:")
print(number_rows)
