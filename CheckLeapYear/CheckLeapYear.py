"""
In this program, you will learn to check whether a year is leap year or not.

A leap year is exactly divisible by 4 except for centry years (years ending with 00).
The century year is a leap year only if it is perfectly divisible by 400
"""

# Python program to check if the input year is a leap year or not

year = int(input("Enter a year: "))

# To get year (integer input) from the user
# Year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if(year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


