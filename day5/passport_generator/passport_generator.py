#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters+1):
  random_letter =random.randint(0, len(letters)-1)
  print(letters[random_letter], end="")
for n in range(0, nr_symbols+1):
  random_symbols = random.randint(0, len(symbols)-1)
  print(symbols[random_symbols], end="")
for x in range(0, nr_numbers+1):  
  random_numbers = random.randint(0, len(numbers)-1)
  print(numbers[random_numbers], end="")
  
#print(letters[random_letter] + symbols[random_symbols] + numbers[random_numbers], end="") bu kodda 3 tane veriyor sadece

#######################
# teacher solution

password=""
#nr_letters = 4
for char in range(1, nr_letters+1):
  #1-4
  # random_char=random.choice(letters)
  # password += random_char
  password=random.choice(letters)
  #print(letters)
  #print(random_char)
for char in range(1, nr_symbols+1):
  password=random.choice(symbols)

for char in range(1, nr_numbers+1):
  password=random.choice(numbers)

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for i in range(0, nr_letters+1):
  random_letter =random.randint(0, len(letters)-1)
  #print("i", i)
  #print(letters[random_letter])
  listem.append(letters[random_letter])
  #print(listem)
for n in range(0, nr_symbols):
  random_symbols = random.randint(0, len(symbols)-1)
  #print("n", n)
  #print(symbols[random_symbols])
  listem.append(symbols[random_symbols])
  #print(listem)
for x in range(0, nr_numbers):  
  random_numbers = random.randint(0, len(numbers)-1)
  #print("x", x)
  #print(numbers[random_numbers])
  listem.append(numbers[random_numbers])
  #print(listem)

random.shuffle(listem)
last=""
for kelime in listem:
  last=last+kelime

print(last)

##################
#teacher solution
password_list = []

for char in range(1, nr_letters+1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(passwor_list)

password=""
for char in password_list:
  password += char

print(f"Your password is: {password}")
