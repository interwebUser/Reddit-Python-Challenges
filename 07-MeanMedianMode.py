# 8/1/2019
# One of many application challenges from the /r/learnpython subreddit of varying degrees of difficulty
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar
import math

# Initialize number list
num_list = []

def get_numbers():
    print("\n\n==============================")
    print("Welcome to Triple-M Calculator")
    print("==============================\n")
    print("Let's start by creating your list of numbers...\n")
    number = input("Enter a number to add to the list: ")
    try:
        number = float(number)
        num_list.append(float(number))
        next_cue = input("Would you like to enter another number (Y/N)? ")
        if next_cue.upper() == "Y":
            get_numbers()
    except ValueError:
        number = input("That's not a number...Enter a number to add to the list: ")

# Get mean
def get_mean(list_of_numbers):
    mean = round(sum(list_of_numbers)/len(list_of_numbers),2)
    print("\nThe mean of the numbers you entered is: " + str(mean) + ".\n")

# Get median
def get_median(list_of_numbers):
    if len(list_of_numbers) % 2 != 0:
        median = list_of_numbers[int(math.floor(len(list_of_numbers)/2))]
        print("The median value is: " + str(median) + ".\n")
    else:
        print("Since there is an even number of values in the list you entered, here are the two median values:")
        lower_median = str(list_of_numbers[int((len(list_of_numbers)/2)-1)])
        upper_median = str(list_of_numbers[int((len(list_of_numbers)/2))])
        print("Lower median value: " + lower_median)
        print("Upper median value: " + upper_median)

# Determine mode
def get_mode(list_of_numbers):
    # Make a list of counts for each element in the list
    count_list = []
    for num in list_of_numbers:
        count = list_of_numbers.count(num)
        count_list.append(count)
        
    # Determine highest occurrances
    highest_occ = max(count_list)
    # Associate highest occurrances with the list of numbers
    # Make a list of indecies for modes
    modes = []
    for count in count_list:
        if highest_occ == count:
            mode_index = count_list.index(count)
            modes.append(mode_index)

    if highest_occ == 0:
            print("There are no repeated values in this list.")
    else:
        for mode in modes:
            print("I've found a mode of " + str(list_of_numbers[mode]) + " at index " + str(mode) + " of the list.")

get_numbers()
# Display Ordered list
num_list.sort()
print("\nI've sorted the list in ascending order. It looks like this: ")
print(num_list)

get_mean(num_list)
get_median(num_list)
get_mode(num_list)