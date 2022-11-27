#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=FunctionDef.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
def Calculate_circumference(radius):
    
    # Calculate the circumference of a circle based on its radius
    return 2 * 3.142 * radius
# Get a radius value as a string
r = input("Provice a radius value")
# convert to a float
r_converted = float(r)
# call the function and return the value
a = Calculate_circumference(r_converted)
print(a)