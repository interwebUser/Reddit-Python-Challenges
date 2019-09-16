# 9/16/2019
# One of many application challenges from the /r/learnpython subreddit of varying degrees of difficulty
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar

import random

print("\n\nWelcome to the Higher-Lower Guessing Game by Khalil Najjar!")
print("The computer will select a random number between 1 and 100")
print("You have to guess the number and the program will let you")
print("know when you've selected the right number or if it's higher")
print("than your guess. Let's get started!\n")

def guessHigherLower():
    numList = range(1,100)
    number = random.choice(numList)
    guessing = True
    guess_count = 0
    while guessing:
        guess = int(input("Make a guess!\n"))
        guess_count += 1
        if guess == number:
            print("You guessed the number " + str(number) + " correctly in "+ str(guess_count) + " tries!")
            play_again = input("Would you like to play again? Y/N\n")
            if play_again.upper() == "Y":
                guessHigherLower()
            else:
                print("\nThanks for playing! Goodbye!\n")
                exit()
        else:
            if guess > number:
                print("Too high!\n")
            if guess < number:
                print("Too low!\n")



guessHigherLower()