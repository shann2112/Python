#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=library2.py
#   Purpose: Modules and packages
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
from math import sqrt
print("Input lengths of the two short triangle sides")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a ** 2 + b ** 2)
print("The length of the hypotenuse to four decimal places is {hypo:1.4f}".format(hypo=c))