vowels = 0
consonants = 0

phrase = input("Type any phrase you wante: ")

for letter in phrase:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels and {} consonants.".format(vowels,consonants))