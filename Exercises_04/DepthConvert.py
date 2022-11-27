#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=my_While.py
#   Purpose: loops and Statements
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
Conversion = 0.3048
Depth = 0
my_depth_in_feet = [12.3,13.8,15.3,12.1,8.8]
my_depth_in_meters = [(depth * Conversion) for depth in my_depth_in_feet]
print(my_depth_in_meters)