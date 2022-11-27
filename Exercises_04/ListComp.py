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
my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)
print(my_list)

my_list2 = [letter for letter in my_string]
print(my_list2)

my_list3 = [number for number in range(0,20)]
print (my_list3)

my_list4 = [number * 10 for number in range(0,20)]
print (my_list4)

my_list5 = [number * 10 for number in range(0,20) if number < 10]
print (my_list5)

