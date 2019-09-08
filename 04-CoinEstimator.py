# 7/29/2019
# One of many application challenges from the /r/learnpython subreddit of varying degrees of difficulty
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar

import time
import math

class CoinsToMoney():
    def __init__(self):
        print("=======================================================")
        print("Welcome to the Coin Wrapper Calculator by Khalil Najjar")
        print("=======================================================\n")

total_value = 0
scale = ""
# penny_weight_g = 2.56
# penny_weight_p = 0.005643834
# nickel_weight_g = 5
# nickel_weight_p = 0.0110231
# dime_weight_g = 2.268
# dime_weight_p = 0.0050000841
# quarter_weight_g = 5.670
# quarter_weight_p = 0.01250021

def get_scale():
    global scale
    scale = input("Would you like to enter your coin weights in grams or pounds (G/P)? ")
    scale = scale.upper()
    if scale == "G":
        print("You've selected to use grams as your weight measurement.\n")
        return
    if scale == "P":
        print("You've selected to use pounds as your weight measurement.\n")
        return
    else:
        print("That's not a valid selection.\n")
        time.sleep(1)
        get_scale()

def pennies():
    global total_value
    global scale
    if scale == "G":
        weight_pennies = input("Please enter the weight of the pennies in grams: ")
        try:
            print("You've entered " + weight_pennies + "g in pennies.")
            weight_pennies = float(weight_pennies)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            pennies()
        penny_count = weight_pennies/2.5
        penny_value = round(penny_count/100, 2)
        total_value += penny_value
        penny_wrapper = math.ceil(penny_count/50)
        print("You have $" + str(penny_value) + " dollars in pennies. You'll need a total of " + str(penny_wrapper) + " wrapper(s).\n")
    if scale == "P":
        weight_pennies = input("Please enter the weight of the pennies in pounds: ")
        try:
            print("You've entered " + weight_pennies + "lbs in pennies.")
            weight_pennies = float(weight_pennies)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            pennies()
        penny_count = weight_pennies/0.005643834
        penny_value = round(penny_count/100, 2)
        total_value += penny_value
        penny_wrapper = math.ceil(penny_count/50)
        print("You have $" + str(penny_value) + " dollars in pennies. You'll need a total of " + str(penny_wrapper) + " wrapper(s).\n")

def nickles():
    global total_value
    global scale
    if scale == "G":
        weight_nickles = input("Please enter the weight of the nickles in grams: ")
        try:
            print("You've entered " + weight_nickles + "g in nickles.")
            weight_nickles = float(weight_nickles)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            nickles()
        nickle_count = weight_nickles/5
        nickle_value = round(nickle_count/20, 2)
        total_value += nickle_value
        nickle_wrapper = math.ceil(nickle_count/40)
        print("You have $" + str(nickle_value) + " dollars in nickles. You'll need a total of " + str(nickle_wrapper) + " wrapper(s).\n")
    if scale == "P":
        weight_nickles = input("Please enter the weight of the nickles in pounds: ")
        try:
            print("You've entered " + weight_nickles + "lbs in nickles.")
            weight_nickles = float(weight_nickles)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            nickles()
        nickle_count = weight_nickles/0.0110231
        nickle_value = round(nickle_count/20, 2)
        total_value += nickle_value
        nickle_wrapper = math.ceil(nickle_count/40)
        print("You have $" + str(nickle_value) + " dollars in nickles. You'll need a total of " + str(nickle_wrapper) + " wrapper(s).\n")

def dimes():
    global total_value
    global scale
    if scale == "G":
        weight_dimes = input("Please enter the weight of the dimes in grams: ")
        try:
            print("You've entered " + weight_dimes + "g in dimes.")
            weight_dimes = float(weight_dimes)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            dimes()
        dime_count = weight_dimes/2.268
        dime_value = round(dime_count/10, 2)
        total_value += dime_value
        dime_wrapper = math.ceil(dime_count/50)
        print("You have $" + str(dime_value) + " dollars in dimes. You'll need a total of " + str(dime_wrapper) + " wrapper(s).\n")
    if scale == "P":
        weight_dimes = input("Please enter the weight of the dimes in pounds: ")
        try:
            print("You've entered " + weight_dimes + "lbs in dimes.")
            weight_dimes = float(weight_dimes)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            dimes()
        dime_count = weight_dimes/0.0050000841
        dime_value = round(dime_count/10, 2)
        total_value += dime_value
        dime_wrapper = math.ceil(dime_count/50)
        print("You have $" + str(dime_value) + " dollars in dimes. You'll need a total of " + str(dime_wrapper) + " wrapper(s).\n")

def quarters():
    global total_value
    global scale
    if scale == "G":
        weight_quarters = input("Please enter the weight of the quarters in grams: ")
        try:
            print("You've entered " + weight_quarters + "g in quarters.")
            weight_quarters = float(weight_quarters)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            quarters()
        quarter_count = weight_quarters/5.670
        quarter_value = round(quarter_count/4, 2)
        total_value += quarter_value
        quarter_wrapper = math.ceil(quarter_count/40)
        print("You have $" + str(quarter_value) + " dollars in quarters. You'll need a total of " + str(quarter_wrapper) + " wrapper(s).\n")
    if scale == "P":
        weight_quarters = input("Please enter the weight of the quarters in pounds: ")
        try:
            print("You've entered " + weight_quarters + "lbs in quarters.")
            weight_quarters = float(weight_quarters)
        except ValueError:
            print("That's not a valid weight.\n")
            time.sleep(1)
            quarters()
        quarter_count = weight_quarters/0.01250021
        quarter_value = round(quarter_count/4, 2)
        total_value += quarter_value
        quarter_wrapper = math.ceil(quarter_count/40)
        print("You have $" + str(quarter_value) + " dollars in quarters. You'll need a total of " + str(quarter_wrapper) + " wrapper(s).\n")

get_scale()
pennies()
nickles()
dimes()
quarters()

total_value = round(total_value, 2)

print("\nThe total value of your coins is $" + str(total_value) + ".\n")