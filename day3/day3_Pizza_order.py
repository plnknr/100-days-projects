# Problem
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

# Expected Output
# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

# CODE
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill =0
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2 
elif size == "M":
  bill = 20 
  if add_pepperoni == "Y":
    bill += 3 
else:
  bill = 25
  if add_pepperoni == "Y":
    bill += 3 

if extra_cheese == "Y":
  bill += 1
  print(f"Your final bill is: ${bill}.")
else:
  print(f"Your final bill is: ${bill}.")

####################
# Angela's Solution
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? "S", "M", or "L"
# add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
# extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# # Your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: ${bill}.")