
# Set whether moter is running flag
Idle = True


def validate_integer(canrun:bool):
    # Loop forever
    while True:
        try:
            if canrun:
                fuel_amount = int(input("Enter fuel amount integer value: "))
                fuel_consumption = int(input("Enter fuel consumption per litre: "))
            else:
                print("The Moter is Idle and we can calculate endurance, switch on the motor")
                break
        except:
            # Bad value,
            print("Error")
            continue
        else:
            if fuel_amount>fuel_consumption:
                endurance = fuel_amount/fuel_consumption
                print(f"Valid input and your endurance in minutes = {endurance}")
                # Good value, exit the loop            
                break
            else:
                print("Your fuel ampunt is less than the consumption rate")
                continue         
        finally:
            # Only runs after the except, continue
            print("Try again - enter an integer value only!")
validate_integer(Idle)