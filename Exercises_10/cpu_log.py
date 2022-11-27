""""
File utilities, forked from the Comm module of SD-Node, written c. 2017
Tested with Python >=3.6
By: JOR
v0.1 26AUG21

1 get the log path 
2 get the file name
3 get a time stamp
4 get cpu info
5 open the file to append and writhe in a looop all info

"""
from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load
from time import sleep
import os

# Check the OS in use, and figure out a log file name and path
#this_os = detect_os() #calls the os_utilities.py gets the OS Name NOT NEEDED AS CALLED IN LOG PATH
log_path = path_name() #calls the file_utilities.py gets the windows log file path
filename = log_file_name(".csv") #calls the file_utilities.py gets the file name
# Loop forever
while True:
# Begin    
    # Sleep for 1 second
    sleep(1)
    # Get a time stamp for this line
    timestamp = log_file_name("") #calls the file_utilities.py
    # Get some information
    information = cpu_load() #calls the os_utilities.py
    # Create a line for the logfile, convert the integer values to string
    logline = timestamp + ":" + str(information[0]) + "," + str(information[1]) + "\n"
    # Now write it to the logfile
    try:
        
        #I foung Log path was not coded in so I added OS and made the directory
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        with open(log_path+filename, "a") as file_handle:
            print(f"logging to {filename}")
            file_handle.write(logline)
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    except OSError:
        print("OS Error")
    except:
        print("General Error")
# End
