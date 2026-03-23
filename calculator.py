print("Simple Calculator")

while True:
    print("\n1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Power")
    print("6 Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        print("Exiting calculator...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    elif choice == 5:
        print("Result:", a ** b)

    else:
        print("Invalid choice")
