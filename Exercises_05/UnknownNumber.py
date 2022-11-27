#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=UnknownNumber.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
def auto_adder(*my_numbers):
    final_number = 0
    for number in my_numbers:
        final_number = final_number + number
    return final_number
print(auto_adder(12,34,23,66,8,99))    