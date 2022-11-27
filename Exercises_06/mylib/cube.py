# This will only show if called from outside the cube function
cube_text = "Yo, time to cube stuff"

def cube(x):
    # This will only show if this function is caled
    if (__name__ =='__main__'):
        print(f"This module is called {__name__} and executes as a standalone script")
    else:
        print(f"This module is called {__name__} and is being called by another script")
    return x*x*x

## this will only run if cube.py is run directly
print(f"The cube vale = {cube(2)}")
