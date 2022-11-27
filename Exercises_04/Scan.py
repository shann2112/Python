#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=Scan.py
#   Purpose: Loops annd Statements
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
scan = {"192.168.3.10":"80","192.168.3.11":"443","192.168.3.55":"22"}
for ipv4, port in scan.items():
    print(f"Found a service on {ipv4} at {port}")
#----------------------------------------------------------