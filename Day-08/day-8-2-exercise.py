#Write your code below this line ๐


def prime_checker(number):
    is_prime = True
    for i in range(2, number//2):
        print(f"{number}%{i} == {number%i}")
        if number % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)

