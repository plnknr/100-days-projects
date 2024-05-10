print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif 12 < age <= 18:
    bill = 7
    print("Please pay $7.")
  else:
    bill = 12
    print("Please pay $12")

  wants_photo = input("Do you want a photo taken? yes or no/n")
  if wants_photo == "yes":
    print("Please pay $3")
    bill +=3
  print(f"Your final bill is {bill}")
  
    
else:
  print("Sorry, you have to grow taller before you can ride")


# == equal to
# != not equal to


# other solution

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")

#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3

#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")
