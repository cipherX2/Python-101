# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

whole = name1+name2

occurence_of_t = whole.count('t')
occurence_of_r = whole.count('r')
occurence_of_u = whole.count('u')
occurence_of_e = whole.count('e')

occurence_of_l = whole.count('l')
occurence_of_o = whole.count('o')
occurence_of_v = whole.count('v')
occurence_of_e = whole.count('e')

occurence_of_true = str(occurence_of_t+occurence_of_r+occurence_of_u+occurence_of_e)
occurence_of_love = str(occurence_of_l+occurence_of_o+occurence_of_v+occurence_of_e)

sum = int(occurence_of_true + occurence_of_love)

if sum < 10 or sum >= 100:
    print(f"Your score is {sum}, you go together like coke and mentos.")
elif sum > 40 and sum < 50:
    print(f"Your score is {sum}, you are alright together.") 
else:
    print(f"Your score is {sum}.")
    