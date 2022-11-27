#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=Scope.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
my_string = "global"

def my_function():
    my_string = "enclosing"
    def nested_function():
        my_string = "local"
        print(my_string)
    nested_function()
    return my_string

#Print the variable my_String
print(my_string)    
#print the output of the function , my_functin
print(my_function())

