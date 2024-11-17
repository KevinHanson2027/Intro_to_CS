"""
1) Write a Python script that, given the string "I love Python!", prints 
(i.e., extracts) the string "Python!" in 3 different ways:

Using the index (hint: you will need to repeat similar instructions)
Using string slicing
Using string slicing with negative indexes
What to submit: Your Python script

2) The Three Threes Challenge!

Start with the program below, run it, then add several more lines similar to this 
one so that you compute at least 5 of the values from 0 through 15 using exactly three threes.
(We ask for only 5 so that you can skip a few if they give you trouble!)

print("0 =", (3 - 3) * 3) 

You may use any of Python's arithmetic operations:

+ addition
- subtraction or negation
* multiplication
/ division
( ) parentheses for grouping
** power
Your task is to find expressions using exactly three number threes (the digit 3) and the allowed 
operations to compute as many integers from 0 to 15 as possible.
"""
# Task 1 
print("Please input: I love Python!")
print("Enter here:")
text = input()
print("")

#Using the index
print("Python!, using the index")
print(text[7:])
print("")

#Using string slicing
print("Python!, using string slicing")
print(text[7:])
print("")

#Using string slicing with negative indexes
print("Python!, using string slicing with negative indexes")
print(text[7:14])
print("")

# Task 2
import math as m 
# Three Threes Challenge
print("0 =", (3 - 3) * 3)
print("1 =", 3 ** (3 - 3))
print("2 =", 3 - 3 / 3)
print("3 =", (3 - 3) + 3)
print("4 =", 3 / 3 + 3)
print("5 =", m.factorial(3) - 3 / 3)
print("6 =", m.factorial(3) * 3 / 3)
print("7 =", m.factorial(3) + 3 / 3)
print("8 =", )
print("9 =", 3 ** 3 / 3)
print("10 =", )
print("11 =", )
print("12 =", )
print("13 =", )
print("14 =", )
print("15 =", )