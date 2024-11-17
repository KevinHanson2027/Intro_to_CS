# Conditional Statements
# Even or Odd
# import math
# x = int(input())
# if x % 2 == 0:
#     print(f"x is true")
# else:
#     print(f"x is false")

# Class Assignment 2
# print("Print a number between 1 and 7")
# number = int(input())

# if number == 1:
#     print(f"Number = Monday")
# elif number == 2:
#     print(f"Number = Tuesday")
# elif number == 3:
#     print(f"Number = Wednesday")
# elif number == 4:
#     print(f"Number = Thursday")
# elif number == 5:
#     print(f"Number = Friday")
# elif number == 6:
#     print(f"Number = Saturday")
# elif number == 7:
#     print(f"Number = Sunday")
# else:
#     print(f"Number = False")

# Class Assignment 3
# print("You will be payed 15$/hour for the first 40 hours, anything after 40 hours will be 50% of your hourly rate")
# print("Please input your hours for this week")
# hours = int(input())
# print("")

# if hours <= 40 and hours > 0:
#     print("Here is you pay:", hours * 15,"$") 
#     print("Enjoy your paycheck!")
# elif hours > 40:
#     max_hrs = 40
#     base_max = (40 * 15)
#     print("Here is you pay:",base_max + ((max_hrs - hours) * (15 * 1.5)),"$")
#     print("Enjoy your paycheck!")
# else:
#     print("Error")

# Class Assignment 4
# print("What did you get on your test?")
# grade = (float(input()))

# if grade >= 90: 
#     print("You got an A")
# elif grade < 90 and grade >= 80:
#     print("You got a B")
# elif grade < 80 and grade >= 70:
#     print("You got a C") 
# elif grade < 70 and grade >= 60:
#     print("You got a D") 
# elif grade < 61 and grade >=0:
#     print("You got a F")
# else:
#     print("Error")

# Class Assignment 5
print("What is your charcters health:")
Health = int(input("Health (In-between 0-100):"))

print("What is your charcters inventory:")
Inventory = str(input("Inventory (Food y/n):"))

print("What is your charcters time of the day:")
Time = str(input("Time (Day/Night):"))

print("")

if Health < 0 or Health > 100:
    print("Invalid Health")
elif Inventory != "y" or Inventory != "n":
    print("Invalid Inventory")
elif Time != "Day" or Time != "Night":
    print ("Invalid Time")

if Health < 30: 
    if Time == "Day":
        print("Your health is low, you should rest")
    else:
        print("Your health is low, you should rest")

if Health > 30:
    if Time == "Day":
        print("Daytime, we should explore!")
    else:
        print("Nighttime, we should eat!")
        
if Inventory == "n":
    if Time == "Day":
        print("Daytime, we should search for food!")
    else:
        print("Nighttime, we should rest")