# #For Loop with Lists
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

#Fizz buzz 3 de fizz 5 de buzz 3 ve 5 de fizzbuzz
for number in range(1,101):
  if number%3==0:
    if number%5==0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)

#teacher solution

target 100
for number in range(1,101):
  if number % 3 and number %5==0:
    print("FizzBuzz")
  elif number % 3==0:
    print("Fizz")
  elif number % 5==0:
    print("Buzz")
  else:
    print(number)