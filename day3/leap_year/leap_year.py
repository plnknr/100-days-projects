# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year%400!=0:
  if year%100!=0:
    if year%4==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Not leap year")
else:
  print("Leap year")

#teacher solution

if year % 4 ==0:
  if year % 100 ==0:
    if year % 400 ==0:
      print("Leap year")
    else:
      print("Not Leap year")
  else:
    print("Leap year")
else:
  print("Not Leap year")