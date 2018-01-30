# LISTS -> []
list1 = [27,46,-5,17,99]

# Lists can have multiple datatypes
list2 = ["A", "B", "C", 1, 2, 3, True, False]

#Lists can have lists inside them - as many levels as you like
list3 = [1, 2, [3, 4, 5], 6, 7, 8]

list4 = [1, [2, 3, [4, 5, 6, [7, 8], 9], 10], 11]

"----------------------------------------------------"

# TUPLES -> ()

#tuples are immutable - they cannot be changed
tuple1 = (1,2,3,"A","B","C")

#you can use tuple notation to assign several variables at once
(A,B,C) = (1,2,3)

"-----------------------------------------------------"

# DICTIONARIES -> {}

# Dictionaries don't have any order. Keys and values are always associated

# There is a key and a value associated to it
# Student name is the key, value is their age
students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}

# Look for things in the dict
Alice_Age = students["Alice"]

# Add entries to the dictionary
    # students["Fred"] = 25 

# Remove entries from the dict
    # del students["Fred"] 

# Get the keys as a list
names = list(students.keys())

# Get the values as a list
ages = list(students.values())

"---------------------------------------------------"

# DICTIONARIES - ADVANCED

# Dictionary with values as lists -> Key:[Values]
students_2 = {
        "Alice":["ID0001", 26, "A"], 
        "Bob":["ID0002", 27, "B"], 
        "Claire":["ID0003", 17, "C"], 
        "Dan":["ID0004", 21, "D"], 
        "Emma":["ID0005", 22, "E"]
        }

# Dictionary with values as dictionaries -> Key:{Key:Value}
students_3 = {
        "Alice":{"ID":"ID0001", "age":26, "grade":"A"}, 
        "Bob":{"ID":"ID0002", "age":27, "grade":"B"}, 
        "Claire":{"ID":"ID0003", "age":17, "grade":"C"}, 
        "Dan":{"ID":"ID0004", "age":21, "grade":"D"}, 
        "Emma":{"ID":"ID0005", "age":22, "grade":"E"}
        }