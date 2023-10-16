import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Invalid input for square root"
    return math.sqrt(x)

def exponentiate(x, y):
    return x ** y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x)

def scientific_calculator():
    while True:
        print("\nScientific Calculator Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Exponentiate")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice == "10":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "6"]:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

        elif choice in ["5"]:
            x = float(input("Enter a number: "))

        else:
            x = float(input("Enter an angle in degrees: ")

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", subtract(x, y))
        elif choice == "3":
            print("Result:", multiply(x, y))
        elif choice == "4":
            print("Result:", divide(x, y))
        elif choice == "5":
            print("Result:", square_root(x))
        elif choice == "6":
            print("Result:", exponentiate(x, y))
        elif choice == "7":
            print("Result:", sin(x))
        elif choice == "8":
            print("Result:", cos(x))
        elif choice == "9":
            print("Result:", tan(x))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    scientific_calculator()
