# Problem
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Expected Output
# Example Input
# 56
# Example Output
# You have 1768 weeks left.


# CODE

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

years = int(90 -int(age))
weeks = years*52

print(f"You have {weeks} weeks left.")

###################
# Teacher Solution

# age = input()
# # Your code below this line 👇
# years = 90 - int(age)
# weeks = years * 52

# print(f"You have {weeks} weeks left.")
