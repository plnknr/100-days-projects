#If the bill was $150.00, split between 5 people, with 12% tip. 
#print("Welcome to the tip calculator.")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#total_bill=print(input("What was the total bill?"))
#people_number=print(input("How many people to split the bill?"))
#Format the result to 2 decimal places = 33.60
#tip_percentage=print(input("What percentage tip would you like to give? 0, 10, 12, or 15?"))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill?"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people_number=int(input("How many people to split the bill?"))
# print(type(total_bill))
# print(type(tip_percentage))
# print(type(people_number))
last_bill = total_bill + ((float(total_bill)* float(tip_percentage)) / 100)
# print(type(last_bill))
each_person_bill = round(float(last_bill / float(people_number)),2)
print(f"Each person should pay: $ {each_person_bill} ")

