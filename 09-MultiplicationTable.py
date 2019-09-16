# 9/16/2019
# One of many application challenges from the /r/learnpython subreddit of varying degrees of difficulty
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar

print("\nWelcome to the Multiplication Tables application by Khalil Najjar.\n")
min = int(input("Please enter the lower value in your square multiplication table: "))
max = int(input("Please enter the upper value in your square multuplication table: "))

x_axis = []
y_axis = []

for i in range(min,max+1):
    x_axis.append(i)
    y_axis.append(i)

print("\nHere's your multiplication table:\n")

for x in range(len(x_axis)):
    print("\n")
    for y in range(len(y_axis)):
        print(x_axis[x]*y_axis[y], ' ', end='')