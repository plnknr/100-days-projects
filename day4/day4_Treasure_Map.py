# Question
# You are going to write a program that will mark a spot on a map with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# CODE
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
x=list(position)
#print(x)
#print(type(x))
if x[0] == "A":
  if x[1] == "1":
    map[0][0] = "X"
  elif x[1] == "2":
    map[1][0] = "X"
  elif x[1] == "3":
    map[2][0] = "X"
elif x[0] == "B":
  if x[1] == "1":
    map[0][1] = "X"
  elif x[1] == "2":
    map[1][1] = "X"
  elif x[1] == "3":
    map[2][1] = "X"
elif x[0] == "C":
  if x[1] == "1":
    map[0][2] = "X"
  elif x[1] == "2":
    map[1][2] = "X"
  elif x[1] == "3":
    map[2][2] = "X"
else:
  print("You entered an invalid position.")
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

################################
# Angela's Solution
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # Your code below
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")