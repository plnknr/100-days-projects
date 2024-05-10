# Problem
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# CODE

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combine_names =name1 + name2
last=combine_names.lower()
z=0
say=0
if "t" in last:
  z=last.count("t")
  say+=z
if "r" in last:
  z=last.count("r")
  say+=z
if "u" in last:
  z=last.count("u")
  say+=z
if "e" in last:
  z=last.count("e")
  say+=z

#print("say:", say)

x=0
y=0
if "l" in last:
  x=last.count("l")
  y+=x
if "o" in last:
  x=last.count("o")
  y+=x
if "v" in last:
  x=last.count("v")
  y+=x
if "e" in last:
  x=last.count("e")
  y+=x

#print("y degeri:", y)

new=str(say)
new1=str(y)
new2=new+new1
#print(type(new2))

#print(f"Your score is {new2}")
newt=int(new2)
if newt<10 or newt>90:
  print(f"Your score is {newt}, you go together like coke and mentos.")
elif 40<newt<50:
  print(f"Your score is {newt}, you are alright together.")
else:
  print(f"Your score is {newt}.")

#######################
# Angela's Solution
# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # Your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")