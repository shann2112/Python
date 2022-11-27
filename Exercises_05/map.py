#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=map.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
my_numbers = [1,2,3,4,5]

def double_number(n: int) -> int:
    return n+n

# Map my numbers to the double_number function, return type is map
result =  map(double_number,my_numbers)
# Print a list of the map
print(list(result))

# Iterate through it
for item in map(double_number,my_numbers):
    print(item)