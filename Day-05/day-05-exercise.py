# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(student_heights)

sum=0
len=0
for i in student_heights:
    # print(i)
    sum+=i
    len+=1

avg = round(sum/len,2)

print(f"The average is {avg}.....")

