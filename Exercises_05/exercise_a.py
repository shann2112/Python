#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=exercise_a.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
# we set up the function. We dont need to put in boolean return value as the return statement will be = or != to 0
def divisible(numerator: int, denominator: int):
    # the return which will be either true or false depending on the remainder value
    return (numerator % denominator == 0)
# we can sent in a value that works, for example (28,4) whick leaves a remainder of 0
# but if it was 30,4 then we get false so you would need to change the return value to be !=0
print (divisible(28,4))