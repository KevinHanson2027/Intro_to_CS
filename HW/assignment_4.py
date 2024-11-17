"""
Write a Python program that asks the user to enter 3 numbers and prints repetitions.

Example 1:
    Input: 3,4,5
    Output: all numbers are different
    Example 2:
Input: 5,4,4
    Output: the user entered 4 twice
Example 3:
   Input: 15,15,15
   Output: the user entered 15 three times
"""
# Task 1 (Input 3 numbers / Prints Repitions):
print("Please enter 3 numbers below")

num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))
num_3 = int(input("Number 3: "))

print("")

if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
    print("all numbers are different")
# Task 2 (Inputs 4 twice / Prints Repitions):
if ((num_1 == num_2 and num_1 == num_3) or (num_2 == num_3 and num_1 == num_3)) and (num_1 != num_2 != num_3):
    print("the user entered a number twice")
# Task 3 (Input 15 three times / Prints Repitions):
if num_1 == num_2 and num_1 == num_3:
    print("the user entered the same number 3 times")