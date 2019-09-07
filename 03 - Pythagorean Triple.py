import time

print("\n=======================================================")
print("Welcome to the Pythagorean Triple Checker Application!")
print("=======================================================\n")

def triples_check():
    try:
        a = int(input("\nInput the length of the first side (a): \n"))
        b = int(input("\nInput the next of a side (b): \n"))
        c = int(input("\nInput the final of a side (c): \n"))
    
        sides = [a, b, c]
        hypotenuse = max(sides)
        organized_sides = []
        for i in range(len(sides)):
            if sides[i] != hypotenuse:
                organized_sides.append(sides[i])

        if organized_sides[0]**2 + organized_sides[1]**2 == hypotenuse**2:
            print("\nYou've entered a pythaorean triple with a hypotenuse length of " + str(hypotenuse) + "! \n")
            retry()
        else:
            print("\nThat combination of sides doesn't compute to a pythagorean triple.\n")
            retry()

    except ValueError:
        print("\nPlease input numbers only.")
        retry()

def retry():
    print("\n============================")
    retry = input("\nWould you like to try again? (Y/N)\n")
    if retry.upper() == "Y":
        triples_check()
    else:
        print("\nThanks for using the Pythagorean Triples Checker!\n")
        exit()

triples_check()