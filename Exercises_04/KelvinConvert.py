#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=my_While.py
#   Purpose: Convert 10 values from Kelvin to Celcius and fahrenheit
#   PreRequisites: Use VSC
#   Revision 1.0
#-------------------------------------------------------------------

# I like to clear the screen first so I import the OS function to use CLS
import os
os.system('cls')

# First lets put in the conversion values from Kelvin 
Kelvin_to_Celsius = -273.15
Kelvin_to_Fahrenheit = -457.87

# lets put in 10 ramdom values
my_Kelvin = [5.25, 2.30, 3.8, 5.3, 2.1, 8.8, 5.52, 8.69, 3.25, 9.52]

# Using code from John's  deptin feet conversion I altered to make it work for me
# I addeed in the round function to bring the values to 2 decimal places
my_Kelvin_in_Cent = [round(Kelvin_to_Celsius + Temp,2) for Temp in my_Kelvin]
my_Kelvin_in_Fahr = [round(Temp2 - Kelvin_to_Fahrenheit,2) for Temp2 in my_Kelvin]

# Lets print the results
print(f"Kelvin converted to Celsius  = {my_Kelvin_in_Cent}")
print(f"Kelvin converted to Fahrenheit = {my_Kelvin_in_Fahr}")

#------------------------------------------------------------------