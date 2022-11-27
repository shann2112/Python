"""
Simple Class by JOR, by convention, use camel case to name classes
"""
# Create a class
class JORzClass():
    # Constructor, called whenever an instance of the class is created.

    #Creates the class and takes in the name variable and sets it to self'    
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)

    
class MickClass():
    #take in two parameters for multiplication
    def __init__(self, Num1:int, Num2:int):
        print("Running constructor for Mick, Hello")
        # do the calculation and store in self.message
        self.message = Num1*Num2

    def my_method(self):
        # Print the total here
        print(self.message)



# initiates class1 from JORzClass and initialises self with passed variable
#my_class1 = JORzClass("Morning JOR!")

# now we have the class inherinted we can use methith from it
#my_class1.my_method()

# Prints the type of class, in this case it is __main__.JORzClass
#print(type(my_class1))


# Construct instance and passin 2 numbers for multiplication
my_class2 = MickClass(Num1=5,Num2=10)
#After passing in 2 numbers lets print the result
# I am a bit confuese why I cant pass variables directly into a cladd function but Im sure this will comee
my_class2.my_method()


