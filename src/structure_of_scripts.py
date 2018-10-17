# Kiewit Project

# Desired scripts layout
 
# Author: Mohammad Abdo
# 10/03/1018


# I am a single line comment, I start by '#'

# Comments should be about 60% of your script.

# Also, please add your name as the Author with the date you started the script


"""
We are multiple
lines comments
"""

'''
We are also Multiple
lines comments
'''


a = 1.0 # I am a simple variable
b = 2.0 


def do_something(x): # This is how you define a function, do not forget the colons
    '''
    Write a detailed discription of the function, what does it do,
    What are the arguments(Inputs), outputs and the discription of each
    
    '''
    print('Your x was {:.2f}'.format(x))# Please notice the indentation
    print('Your a, b were {:.2f}, {:.2f} respectively'.format(a,b))
    if x > 200: 
        return b*x
    else:
        return a*x
     
if __name__ == '__main__':
    out = do_something(111)
    print(do_something(245))