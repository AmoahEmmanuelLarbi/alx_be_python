"""
Create a Python script named arithmetic_operations.py. 
In this script, define a function that performs basic arithmetic operations. 
This function, perform_operation, will be imported and used in a separate main.py script, which we provide.
"""

#define a function that performs basic arithmetic operations
def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Supported values are "add", "subtract", "multiply", "divide".

    Returns:
        float: The result of the arithmetic operation, or None if an error occurs.

    Exceptions:
        Prints an error message if division by zero is attempted or if an invalid operation is provided.
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                print("Can't divide by zero")
            elif num2 != 0:
                return num1 / num2
        case _:
            print("Invalid operation")

#testing
#result = perform_operation(5, 6, "add")
#print(result)