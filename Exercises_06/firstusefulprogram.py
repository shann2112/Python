#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=firstusefulprogram.py
#   Purpose: Modules and packages
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
import platform

def detect_os()->str:
    # Detect the OS in use
    return platform.system()

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    #check the OS file in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()

    # Parse the response
    if my_os == "windows":
        print("Your system is windows")
    elif my_os == "linux":
        print("Your system is linux")
    elif my_os == "darwin":
        print("Your apple system is MacOs")
    elif my_os == "cygwin":
        print("Your Apple system is MacOS")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        print(f"Unidentified system = {my_os}")
else:
    print(f"This module is called {__name__} and is being caled from another script")