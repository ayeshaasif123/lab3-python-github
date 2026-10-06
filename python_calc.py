def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


def percentage(value, total):
    if total == 0:
        return "Error: Total cannot be zero."
    return (value / total) * 100


while True:
    print("\n--- Python Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", divide(a, b))

    elif choice == "5":
        n = int(input("Enter a number: "))
        print(n, "is", even_odd(n))

    elif choice == "6":
        value = float(input("Enter obtained value: "))
        total = float(input("Enter total value: "))
        result = percentage(value, total)
        if isinstance(result, str):
            print(result)
        else:
            print("Percentage:", result, "%")

    elif choice == "7":
        print("Thank you for using the calculator.")
        break

    else:
        print("Invalid choice. Please try again.")
