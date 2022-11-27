#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=globalkeyword.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
my_string = "global"

def my_functon():
    global my_string
    print(f"At the moment, my_string id {my_string}")
    my_string = "Mangled"

my_functon()
print(f"Now the value of my_string = {my_string}")