# This will only show if called from outside the square function
square_text = "Yo, time to square stuff"

def square(x):
    # This will only show if this function is caled
    if (__name__ =='__main__'):
        print(f"This module is called {__name__} and executes as a standalone script")
    else:
        print(f"This module is called {__name__} and is being called by another script")
    return x*x

## this will only run if square.py is run directly
print(square(2))