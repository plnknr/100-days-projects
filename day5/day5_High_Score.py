# Question
# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x
# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91

# CODE
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

############################
# Angela's Solution
# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
#     # print(highest_score)

# print(f"The highest score in the class is: {highest_score}")