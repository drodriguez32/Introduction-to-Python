# get sentence from user
original = input("Please write the sentence you want to translate: ").strip().lower()

# split sentence into words
words = original.split()

# loop through words and convert to Pig Latin
new_words = []
    
for w in words:
    
    # if it starts with a vowel just add "yay" to the end
    if w[0] in "aeiou":
        n_w = w + "yay"
        new_words.append(n_w)
        
    # if it starts with consonants, move the consonants to the end and add "ay"
    else:
        vowel_pos = 0
        for letter in w:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = w[:vowel_pos]
        rest = w[vowel_pos:]
        
        n_w = rest + cons + "ay"
        new_words.append(n_w)

# stick words back together
pig_sentence = " ".join(new_words)

# print the final string
print("\n", pig_sentence)

