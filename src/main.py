# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:19:33 2018

@author: mgabdo
"""

# This file is just a template if you tried to run it it won't run as these functions are not built yet.



#import make_calculations

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
    pass

def make_outputs():
    '''
    Describe
    '''
    
    pass



if __name__ == '__main__':
    
    x,y = read_user_inputs(2e5,300)
    m,n = read_pipe_data('/home/mgabdo/ME575/Kiewit/inputs/pipedata/foo.txt')
    tbl = read_arrow_tables('/loc/of/tables/spitted/by/arrow')
    #make_calculationes(x,y,m,n,tbl)
    make_outputs()