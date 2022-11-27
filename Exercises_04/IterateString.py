#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=MyNumber.py
#   Purpose: loops and Statements
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
# Define a string to iterate over
for this_letter in "Michael Shannon":
    #Specify which letter to test
    if this_letter == "n":
        # Found the test letter
        print(f"Woo Hoo, found a {this_letter}!")
        # Exit the current loop
        break
    else:
        # Didn't find the test letter
        print(f"Aww man, I didn't want a {this_letter}!")