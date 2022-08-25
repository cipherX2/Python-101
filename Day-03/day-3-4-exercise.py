# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# pepperoni_small_pizza=2
# pepperoni_other_pizza=3


total_bill=0

if size == "S":
    total_bill=15
elif size == "M":
    total_bill=20
else:
    total_bill=25

if add_pepperoni == "Y" and size == "S":
    total_bill+=2
if add_pepperoni == "Y" and size == "M" or size == "L":
    total_bill+=3
if extra_cheese == "Y":
    total_bill+=1

print(f"Your total bill is ${total_bill}")


