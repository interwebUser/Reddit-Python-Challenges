# 9/16/2019
# One of many application challenges from the /r/learnpython subreddit of varying degrees of difficulty
# Link: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/
# Created by Khalil Najjar

nth_digit = int(input("\n\nPlease type the nth item in the Fibonacci sequence you would like to find: "))

sequence = [0, 1]

print(list(range(nth_digit)))

for i in range(nth_digit):
    sequence[i] = sequence[i-1] + sequence[i-2]
    sequence.append(sequence[i])

print(sequence)
print(sequence[nth_digit])