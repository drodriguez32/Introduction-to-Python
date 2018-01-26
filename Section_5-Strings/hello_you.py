# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:11:11 2018

@author: Diego Rodriguez

---------------------------------------------
"""

# Ask user for name

name = input("What is your name?: ")

# Ask user for age

age = input("What is your age?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy

love = input("What do you enjoy doing?: ")

# Create output text

string = ("Your name is {} and you are {} years old. You live in {} and you enjoy {}.")
output = string.format(name,age,city,love)

# Print output to screen

print ("\n" + output)