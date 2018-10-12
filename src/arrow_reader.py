# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#CSV Method

import pandas as pd
import numpy as np
import subprocess as sp
sp.call(['C:\AFT Products\AFT Arrow 5 Viewer\ArrowViewer.exe'])

adf = pd.read_csv('ArrowModelData.csv',names=list(range(0,100)))
adf = adf.replace(np.nan, '')
adf= adf.set_index(0)
#Creates Pipe Input Data Frame
pidf=adf.loc['Pipe Input Table':'Pipe Fittings & Losses']
pidf=pidf[:-1]
#Turns Pipe Input Data Frame into a Dictionary

#Creates Pipe Fitting and Loss Data Frame
pfdf=adf.loc['Pipe Fittings & Losses':'Area Change Table']
pfdf=pfdf[:-1]


#Excel Method
    # load the spreadsheet
    #ad = pd.read_excel('Arrow Data.xlsx')
    # replace nan with blanks
    #ad = df.replace(np.nan, '')
    # rename indexes to the Pipe names
    #ad = df.set_index('Pipe')
    # Build a global dictionary for pipe information
    #ADict = ad.to_dict()