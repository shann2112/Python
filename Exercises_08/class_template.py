
class MyTemplate():
    # Some variables for the future
    class_object_attribute1 = None
    class_object_attribute2 = None
    
    # Constructor, called whenever an instance of the class is created. Nothing passed in at this stage
    def __init__(self) -> None:
        pass
        
    
    # Test Function to pass in direct values
    def my_method2(self, my_name:str):
        print(f"Good morning {my_name}")
        

# Instantiate the class, I lesft it blank for now, but we can use SELF, and variables
my_object = MyTemplate()
print(type(my_object))
my_object.my_method2("Holly")