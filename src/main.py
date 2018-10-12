# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:19:33 2018

@author: mgabdo
"""

# This file is just a template if you tried to run it it won't run as these functions are not built yet.



#import make_calculations

import pandas as pd
import numpy as np

def read_heat_balance(excelfilename,case=None):
    # load the spreadsheet
    df = pd.read_excel(excelfilename)
    # replace nan with blanks
    df = df.replace(np.nan, '')
    # rename indexes to the rel indexes
    df = df.set_index('Unnamed: 1')
    # rename columns to the case name
    df = df.rename(columns=df.loc["Case Name",:])
    # Build a global dictionary for all cases
    Dict = df.to_dict()
    # extracts the required case and build case dictionary
    DictCase = []
    if case is not None:    
        DictCase = Dict[case]
    
    return df,Dict,DictCase
    
def read_user_inputs(P = 1e5 ,T = 300):
    '''
    Describe
    '''
    
    return 2*P, 5*T

def read_pipe_data(filename, what_to_read=None):
    '''
    Describe
    '''
    out1 =10
    out2 = 20
    return out1,out2

def read_arrow_tables(filename):
    '''
    Describe
    '''
    # load the spreadsheet
    ad = pd.read_excel('Arrow Data.xlsx')
    # replace nan with blanks
    ad = df.replace(np.nan, '')
    # rename indexes to the Pipe names
    ad = df.set_index('Pipe')
    # Build a global dictionary for pipe information
    ADict = ad.to_dict()
    
    return ad,ADict
    pass

def make_outputs():
    '''
    Describe
    '''
    
    pass



if __name__ == '__main__':
    df = read_heat_balance("..\inputs\mcInput_hb5.0_hb.xlsx")
    df,Dict,DictCase = read_heat_balance("..\inputs\mcInput_hb5.0_hb.xlsx","Case S-025-G")
    
    #x,y = read_user_inputs(2e5,300)
    #m,n = read_pipe_data('/home/mgabdo/ME575/Kiewit/inputs/pipedata/foo.txt')
    #tbl = read_arrow_tables('/loc/of/tables/spitted/by/arrow')
    #make_calculationes(x,y,m,n,tbl)
    #make_outputs()