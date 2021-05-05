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
import ast

#Create a data frame with each CSV file 

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

resto_naics={"722110": "Full-Service Restaurants",
             "722211": "Limited-Service Resturants",
             "722212": "Cafeterias",
             "722213": "Snack and Nonalcoholic Beverage Bars",
             "722310": "Food Service Contractors",
             "722320": "Caterers",
             "722330":" Mobile Food Services",
             "722410": "Drinking Places (Alcoholic Beverages)"}

#restoloans=allloans['NAICSCode'].apply(ast.literal_eval).str.get('resto_naics')


