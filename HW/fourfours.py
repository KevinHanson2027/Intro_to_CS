# Problem description: The four fours challenge!

'''
    The four fours challenge!    
    Start with the program below, run it, then add several more lines similar to this one 
    so that you compute at least 16 of the 20 values from 0 through 20 using exactly four fours. 
    (We ask for only 16 so that you can skip a couple if they give you trouble!) 
    You may use any of Python's arithmetic operations:
        +    addition
        -    subtraction or negation
        *    multiplication
        /    division
        (   )    parentheses for grouping
        **    power 

    Results with decimals: 1.0, 2.0, etc. are totally ok!
    You may also use 44 or 4.4, each of which count as two fours,
    or .4, which counts as one four.
    or, sqrt, for example sqrt(4) (or others)
    or, factorial, for example factorial(4) (or others)
    both sqrt and factorial are from Python's math library
    aside: the line from math import * is what imports that math library... 

    Here are what the results, but not the source code, will look like.
    Remember you need only 16 of them (0 to 15 == 16):

    Zero is 0
    One is 1
    Two is 2
    Three is 3
    Four is 4
    Five is 5
    Six is 6
    Seven is 7
    Eight is 8
    Nine is 9
    Ten is 10
    Eleven is 11
    Twelve is 12
    Thirteen is 13
    Fourteen is 14
    Fifteen is 15

    You may find the four fours game addicting, or frustrating, or both! Hint: the power operator is helpful!
'''
# Intialize Math Package
import math as m

# Task 1
print("Zero is", 4 + 4 - 4 - 4)
print("One is", 4 / 4 * 4 / 4)
print("Two is", 4 / 4 + 4 / 4)

print("Three is", m.sqrt(4))
print("Four is",)
print("Five is", 4 + 4/4)
print("Six is", m.factorial(4) / 4)

print("Seven is", 4 + 4 - (4/4))

print("Eight is", 4 + 4)

print("Nine is", 4 + 4 + (4/4))
print("Ten is", 4 + 4 + (m.sqrt(4)))

print("Eleven is",4 + 4 + (m.sqrt(4) + 4/4))
print("Twelve is", m.factorial(4) / (m.sqrt(4)))
print("Thrirteen is", m.factorial(4) / (m.sqrt(4)) + (4/4))
print("Fourteen is", m.factorial(4) / (m.sqrt(4)) +(m.sqrt(4) * 4/4))
print("Fifteen is", m.factorial(4) / (m.sqrt(4)) +(m.sqrt(4)) + 4/4)
print("Sixteen is", 4*4)