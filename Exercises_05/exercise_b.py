#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=exercise_b.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------

from unittest import result
from xmlrpc.client import boolean

# I removed Pass and put in return False if the number was not found in the kllist
# pass does nothing.
# as there was no original return False value we got None.

def find_num(number_list:list, number: int)->boolean:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            #pass
            # this will return False now
            return False

result = find_num([1,2,3,4,5,6,7,8],9)   
print(result) 

