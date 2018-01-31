import random as rm

questions = ["Why is the sky blue?",
             "Why does the moon shine?", 
             "Why do we have night and day?",
             "Why is DISISMEC so boring?",
             "Why does the sun shine?"]

question = rm.choice(questions)
answer = input("{}: ".format(question)).strip().lower()

while answer != "just because":
    answer = input ("Why?: ").strip().lower()

print ("Oh... Okay")