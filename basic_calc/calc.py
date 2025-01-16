### Building the Basic Calculator

# Function for Addition
def addition(x,y):
    add_result = x + y
    return add_result

# Function for Subtraction
def subtract(x,y):
    sub_result = x-y
    return sub_result

# Function for Multiplication
def multiply(x,y):
    multy_result = x * y
    return multy_result

# Function for Division
def division(x,y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x/y

def main():
    print("Welcome to the Basic Calculator!")

    while True:
        try:
            num1 = 23
            num2 = 34
        except ValueError:
            print("Invalid value")
            continue
        # Display available operations
        print("\nSelect Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Chosse Operation (1/2/3/4):")

        # Perform the chosen operation
        if operation == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
        else:
            print("Invalid input! Please choose a valid operation.")
        
        # Ask if the user wants to perform another operation
        next_calculation = input("\nDo you want to perform another calculation? (yes/no):")

        if next_calculation.lower() != 'yes':
            print("Thank you for using the Basic Calculator!")
            break
if __name__ == "__main__":
    main()