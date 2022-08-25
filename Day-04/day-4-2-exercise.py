import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(names)
# print(len(names))

length_of_list = len(names)
random_index = random.randint(0,length_of_list-1)

person_paying_bill = names[random_index]

print(f"{person_paying_bill} is going to buy meal today......")
