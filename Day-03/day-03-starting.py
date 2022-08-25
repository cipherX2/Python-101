print("Welcome to the rollercoaster ride....")
height = int(input("Enter your height in cms: "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Pay $5 at the counter...")
    elif age < 18:
        print("Pay $7 at the counter...")
    elif age >= 45 and age <= 55:
        print("This ride is free for you sir.....THANKS FOR COMING....")
    else:
        print("Pay $12 at the counter...")
    wants_photo = input("Do you want some nice photos? type Y or N : ")
    
    if wants_photo == "Y":
        print("Pay $2")
else:
    print("Sry this ride is not for you!")
