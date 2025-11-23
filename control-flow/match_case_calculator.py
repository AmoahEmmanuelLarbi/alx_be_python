"""
Task Description:
Develop a Python script named match_case_calculator.py. 
This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). 
The script will then perform the selected operation using a Match Case statement and display the result.
"""
#solution
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number:  "))

#choose an operation
operation = input("Choose the operation (+, -, *, /): ")
result = 0
#using match case to perform calculation based on chosen operation
match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        if second_number == 0:
            print("Cannot divide by zero")
        else:
            result = first_number / second_number
    case _:
        print("Invalid operation")

print(f"The result is {result}")
