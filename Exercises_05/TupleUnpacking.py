#-----------------------------------------
#   Michael Shannon
#   l00177543
#   l00177543@atu.ie
#   LY_ICTEC_G_INFS_IT903_5_2022
#   Lecturer John ORow
#   Script Name=TupleUnpacking.py
#   Purpose: Functions
#   PreRequisites: Use VSC
#   Revision 1.0
#------------------------------------------
def most_expensive(price_list):
    # Iterate through list and find most expensive item
    # Set up the variables
    max_price = 0
    max_price_item = ""
    
    # Iterate unpacking the tuple
    for description, price in price_list:
        # if this is the maxs price then record it in our varaibles
        if price > max_price:
            max_price = price
            max_price_item = description
        # If it is not the max price then just pass on
        else:
            pass
    # Return the max Price and its description
    return max_price_item, max_price

#provice the data
price_list = [("Pinapple",1.0),("Apples",1.50),("Pears",.70),("Peaches",.80)]
# Call the function and Unpack its return values
product, price = most_expensive(price_list)
print(product,price)












