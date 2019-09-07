# 7/21/2019
# First of 99 application challenges from the /r/learnpython subreddit
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar
# First project ever created in Python

name_of_beer = str(input("\n\nWhat's the name of the beer on the wall?\n"))
initial_bottles = int(input("How many bottles of " + name_of_beer + " are on the wall?\n"))
number_of_bottles = initial_bottles
less_bottles = number_of_bottles - 1


while number_of_bottles > 0:
    if number_of_bottles > 2:
        print("\n" + str(number_of_bottles) + " bottles of " + name_of_beer + " on the wall. " + str(number_of_bottles) + " bottles of " + name_of_beer + ". Take one down, pass it around. " + str(less_bottles) + " bottles of " + name_of_beer + " on the wall!")
    elif number_of_bottles == 2:
        print("\n" + str(number_of_bottles) + " bottles of " + name_of_beer + " on the wall. " + str(number_of_bottles) + " bottles of " + name_of_beer + ". Take one down, pass it around. " + str(less_bottles) + " bottle of " + name_of_beer + " on the wall!")
    elif number_of_bottles == 1:
        print("\n" + str(number_of_bottles) + " bottle of " + name_of_beer + " on the wall. " + str(number_of_bottles) + " bottle of " + name_of_beer + ". Take one down, pass it around. " + "No more bottles of " + name_of_beer + " on the wall!")
    number_of_bottles -= 1
    less_bottles -=1

print("\n\nWe just sang the song: \"" + str(initial_bottles) + " bottles of " + name_of_beer + " on the wall!\"\n")