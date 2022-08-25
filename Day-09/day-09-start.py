# Introduction to dictionaries 

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

# Adding new items

programming_dictionary["Loop"] = "The action of something doing over and over again."
# print(programming_dictionary)

# Creating empty dictionary 

empty_dictionary = {}
# print(empty_dictionary)

# Delete an entire dictionary 

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary

programming_dictionary["Bug"] = "A moth in the computer."
# print(programming_dictionary)

# Looping through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

