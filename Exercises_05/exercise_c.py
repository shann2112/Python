#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=exercise_c.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------

from unittest import result
from xmlrpc.client import boolean

def find_num(number_list:list, number: int)->boolean:
    # iitialise variable to be false
    found_evennumber = False
    # go through the list
    for iterate_number in number_list:
        # mod 2 and no remainder then it is even
        if iterate_number % number == 0:
            # mark the variable as True
            found_evennumber = True
    # Otherwise the variable stays False
    return found_evennumber

# put a list of numbers together and put in 2 as the denominator if it is evenly divisible then it is even
result = find_num([1,3,5,7,8],2)   
print(result) 

