from calculator_art import logo

print(logo)

def add(n1,n2):

    return n1 + n2

def subtract(n1,n2):

    return n1 - n2

def multiply(n1,n2):

    return n1 * n2

def divide(n1,n2):

    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
} 

def calculator():

    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue == True:
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        func = operations[operation]
        result = func(num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower() == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()
