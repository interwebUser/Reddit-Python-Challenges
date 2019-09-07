import math
import os
import time

print("\n================================")
print("Welcome to the Change Calculator")
print("================================\n")

def calculate_change():
    price = input("Enter the total price of sales: ")
    received = input("Enter the amount given to you: ")

    #get change
    change = float(received)-float(price)
    change = float(change)

    #calculate quarters change and value
    quarter_change = math.floor(change/0.25)
    quarters_value = quarter_change * 0.25
    print("Value of Quarters: " + str(quarters_value))

    #calculate dimes change and value
    dimes_change = math.floor((change-quarters_value)/0.1)
    dimes_value = dimes_change * 0.1
    print("Value of Dimes: " + str(dimes_value))

    #calculate nickels change and value
    nickels_change = math.floor((change-quarters_value-dimes_value)/0.05)
    nickels_value = nickels_change * 0.05
    print("Value of Nickels: " + str(nickels_value))

    #calculate pennies change
    pennies_change = round((change-quarters_value-dimes_value-nickels_value)/0.01,2)
    pennies_value = pennies_change * 0.01
    print("Value of Pennies: " + str(pennies_value))

    #print results
    print("\nYou need to return " + str(quarter_change) + " quarters, " + str(dimes_change) + " dimes, " + str(nickels_change) + " nickles,", "and " + str(pennies_change) + " pennies.\n\n")
    
    retry = input("Would you like to calculate the change for another transaction (Y/N)? ")
    if retry.upper() == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
        calculate_change()
    else:
        exit

calculate_change()