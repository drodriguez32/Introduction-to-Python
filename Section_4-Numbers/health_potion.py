#Project 1
import random as rm

health = 50 #initial health of the player

difficulty = 0 #difficulty defined as a number from 1-3 where 1 is easy

print("Input difficulty level - must be a value from 1 to 3")
user_input = int(input())

if (user_input >= 1 and user_input <= 3):
    difficulty = user_input
else:
    print("Difficulty was not changed. Must be a number between 1 and 3")
    print("Please set difficulty again")
    user_input = int(input())
    difficulty = user_input

potion_health = int(rm.randint(25,50) / difficulty) #amount of health that will be added to the player

health_new = health + potion_health #new health value for player after taking the potion

print("Health potion has been found, take it? [y/n]")
take_potion = input()
if take_potion == "y":
    health = health_new
    print("New health:" , health)