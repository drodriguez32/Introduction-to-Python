# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:59:37 2018

@author: Diego Rodriguez
"""

# string.method()

text = "happy birthday"
number_a=text.count("a")

# change case

x = "HAPPY birthday"
x_l = x.lower()
x_u = x.upper()
x_c = x.capitalize()
x_t = x.title() 

# search for pieces of text -> case sensitive

x.index("birthday") # where the word starts
x.find("birthday") # where the word starts -> it doesn't crash if it doesn't find the word (it gives -1)

# strip pieces of text from the sides

y = "000000happybirthday0000"
y.strip("0")
y.lstrip("0") # from the left
y.rstrip("0") # from the right