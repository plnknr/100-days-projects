rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
picture= [rock, paper, scissors]
print("Welcome to the Rock, Paper and scissors game")

user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(f"Your choice is {user_choice}.")
# print(picture[user_choice])

computer_choice =random.randint(0,2)
# print(f"Computers choice is {computer_choice}.")
# print(picture[computer_choice])
if user_choice >= 3 or user_choice <0:
  print("You typed an invalid number, you lose.")
else:
  print(f"Computers choice is {computer_choice}.")
  print(picture[computer_choice])
  print(f"Your choice is {user_choice}.")
  print(picture[user_choice])
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice == 2 and computer_choice == 1:
    print("You win!")
  elif user_choice == 1 and computer_choice == 0:
    print("You win!")
  elif user_choice == computer_choice:
    print("It's a draw")
  else:
    print("You lose!Try again.")

  # print(f"Computers choice is {computer_choice}.")
  # print(picture[computer_choice])
  # print(f"Your choice is {user_choice}.")
  # print(picture[user_choice])

# Teacher solution
if user_choice >= 3 or user_choice <0:
  print("You typed an invalid number, you lose.")
elif user_choice ==0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose!")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")

elif computer_choice == user_choice:
  print("It's a draw")
elif user_choice >= or user_choice <0:
  print("You typed an invalid number, you lose.")