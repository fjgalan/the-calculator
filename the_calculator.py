import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def ln(x):
    if x <= 0:
        raise ValueError("Cannot take the natural logarithm of non-positive numbers")
    return math.log(x)

def log10(x):
    if x <= 0:
        raise ValueError("Cannot take the logarithm of non-positive numbers")
    return math.log10(x)

calculus = {
    'operations': {
        'a': "Addition",
        'b': "Subtraction",
        'c': "Multiplication",
        'd': "Division",
        'e': "Power",
        'f': "Natural Logarithm",
        'g': "Logarithm Base 10"
    },
    'accepted_inputs': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'function': { # llama a las funciones definidas al inicio
        'a': add,
        'b': subtract,
        'c': multiply,
        'd': divide,
        'e': power,
        'f': ln,
        'g': log10
    }
}

unary_ops = ['f', 'g']

print("\nWelcome to The Calculator!\n")

c = calculus

while True:

    for key, values in c['operations'].items(): # muestra las opciones
        print(f"{key}) {values}")

    choice = input("\nPlease, enter your operation of choice, or write 'exit' to quit: ").lower()

    if choice == "exit":
        print("\nOkay, goodbye!\n")
        break

    word_to_letter = {
        "addition": "a",
        "subtraction": "b",
        "multiplication": "c",
        "division": "d",
        "power": "e",
        "natural logarithm": "f",
        "logarithm base 10": "g"
    }
    
    choice = word_to_letter.get(choice, choice)

    while choice not in c['accepted_inputs']:
        print("Invalid input. Please try again.")
        choice = input("Enter your operation of choice: ").lower()
    
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice not in unary_ops:
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    operation = c['function'].get(choice)

    try:
        if choice in unary_ops:
            result = operation(num1)
        else:
            result = operation(num1, num2)
    except ValueError as e:
        print(f"\nError: {e}\n")
        continue
    else:
        print(f"\nThe result is: {result:.3f}\n")