# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:19:33 2018

@author: mgabdo
"""

# This file is just a template if you tried to run it it won't run as these functions are not built yet.



#import make_calculations

import pandas as pd
import numpy as np
#import os
#import pressure_temp_combo


def read_heat_balance(excelfilename, case=None):
    # load the spreadsheet
    df = pd.read_excel(excelfilename)
    # replace nan with blanks
    df = df.replace(np.nan, '')
    # rename indexes to the rel indexes
    df = df.set_index('Unnamed: 1')
    #rename columns to the case name
    df = df.rename(columns=df.loc["Case Name",:])
    #Converst all numeric type value in entire whole DataFrame to float values.
    #Columns that cannot (e.g. they contain non-digit strings or dates) will be left alone.
    df = df.apply(pd.to_numeric, errors='ignore')
    #Locate indexes from HRSG HP Steam to HP Steam Desuperheating Flow
    df = df.loc['HRSG HP Steam':'HP Steam Desuperheating Flow']
    #Remove rows which are not Flow, Pressure and Temperature Values
    df = df[:-2]
    #Sets indicies equal to Flow, Pressure, and Temp for HP HRSG
    df = df.set_index(0)
    # rename columns to the case name
#    df1 = df1.rename(columns=df.loc["Case Name",:])
    # Build a global dictionary for all cases
    Dict = df.to_dict()
    # extracts the required case and build case dictionary
    DictCase = []
    if case is not None:    
        DictCase = Dict[case]
    #max_massflow_case = df.idxmax(0, "HRSG HP Steam")
    #for max_massflow_case:
    #df.loc[df['case'] == 'Pressure, psia']
    #df.loc[df['case'] == 'Temperature, F']
    
    
    
    return df,Dict,DictCase#,massflow_design,pressure,temperature
    
#def read_user_inputs(target_cfr = None, plant_config = None, NPS = None, schedule = None):
#    '''
#    Describe
#    '''
#    pressure_temp_combo(.....)
#    return vel_min_sb
#
#def read_pipe_data(filename, what_to_read=None):
#    '''
#    Describe
#    '''
#    out1 =10
#    out2 = 20
#    return out1,out2
#
#def read_arrow_tables(filename):
#    '''
#    Describe
#    '''
#    #Opens Arrow through given executable path of Arrow
#    os.sys('arrow main.py')
#    #Arrow opens pipe file
#    
#    #Arrow saves data as .csv
#    
#    return csv

def steam_table_lookups():
    '''
    Describe
    '''
    pass

def make_outputs():
    '''
    Describe
    '''
    
    pass



if __name__ == '__main__':
    df = read_heat_balance("../inputs/mcInput_hb5.0_hb.xlsx")
    df,Dict,DictCase = read_heat_balance("../inputs/mcInput_hb5.0_hb.xlsx")
    i=0
    HP_massflow=np.zeros((len(df.columns)-1,1))
    for j in df.columns[1:]:
        HP_massflow[i] = Dict[j]['Flow, lb/h']
        i+=1
        print(HP_massflow)
    HP_massflow_max = max(HP_massflow)
    loc_max = np.argmax(HP_massflow)
    HP_temp = np.zeros((len(df.columns)-1,1))
#    for "Flow, lb/h" in sorted(dict.keys()):
#        print key, dict[key]
#    
#    for j in df.columns[2:]:
#        HP_temp[i] = Dict[j]['Temperature, F']
#    HP_temp_max = 
#    Dict[df.columns[]]
'Pressure, psia'
'Temperature, F'
    #csv1 = read_arrow_tables(filename)
    # read NPS, schedule from csv
    #NPS=..
    #schedule = ..
    #read_user_inputs(,,NPS,schedule)
    #x,y = read_user_inputs(2e5,300)
    #m,n = read_pipe_data('/home/mgabdo/ME575/Kiewit/inputs/pipedata/foo.txt')
    #tbl = read_arrow_tables('/loc/of/tables/spitted/by/arrow')
    #make_calculationes(x,y,m,n,tbl)
    #make_outputs()