# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:20:04 2018

@author: Diego Rodriguez
-------------------------------------------
"""

# Ask user for email address

email = input("Please type your email address: ").strip()

# slice out username

username = email[:email.index("@")]

# slice domain name

domain = email[email.index("@")+1:]

# format message

output = "Your username is {} and your domain name is {}".format(username,domain)

# display output message

print("\n" + output)