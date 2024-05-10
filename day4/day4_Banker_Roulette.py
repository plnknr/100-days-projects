# Question
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

# HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# CODE
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

num_items=len(names)
#print(num_items)
a=random.randint(0,num_items-1)
b =names[a]
print(f"{b} is going to buy the meal today!")

# num_items = len(names)
# random_choice = random.randint(0,num_items-1)

# person_who_will_pay =names[random_choice]

# print(person_who_will_pay + "is going to buy the meal today!")

###########################
# Angela's Solution
# names = names_string.split(", ")

# import random

# # Get the total number of items in list.
# num_items = len(names)
# # Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])