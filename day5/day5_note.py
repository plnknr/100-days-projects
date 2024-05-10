  # Input a Python list of student heights
  student_heights = input().split()
  for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
  # 🚨 Don't change the code above 👆

  # Write your code below this row 👇
  count=0
  sum=0
  #print(type(student_heights))
  for i in student_heights:
    count+=1
    #print(count)
    sum+=student_heights[count-1]
    #print(sum)

  average_height = round(sum /count)

  print("total height =",sum)
  print("number of students =",count)
  print("average height =",average_height)



#2.soru
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

#print(type(student_scores))
new_top=0
count=0
for i in student_scores:
  if student_scores[count]>new_top:
    new_top = student_scores[count]
    #print("new_top:", new_top)
    count+=1
  else:
    #print("aynı kaldı")
    count+=1
print("The highest score in the class is:", new_top)



#For Loop with Range
#for number in range(1 ,11, 3):
 # print(number)

# for number in range(a,b):
#   print(number)

total = 0
for number in range(1,101):
  total += number
print(total)

#3. soru
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇


sum=0
for i in range(2,target+1,2):
  # print("i değeri")
  # print(i)
  sum=sum+i
  # print("sum degeri")
  # print(sum)

print(sum)

#3. soru 2. yol
for number in range(1, target+1):
  if number % 2 == 0:
    sum += number

print(sum)
