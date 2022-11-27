# import both libraries and rename the instance name
import mylib.cube as mycube
import mylib.square as mysquare

# This print statement will get the text from the imorted files which is outdied the function
# then the print statement will call the function and pass in a different variable.
# by doing this from this project the name of the module will be passed back to dsay it was called externally. 
print(mycube.cube_text, mycube.cube(3))
print(mysquare.square_text,mysquare.square(3))
