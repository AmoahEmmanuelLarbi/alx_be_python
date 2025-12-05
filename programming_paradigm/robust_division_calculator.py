"""
Docstring for alx_be_python.programming_paradigm.robust_division_calculator

Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

Task Description:
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.
"""

"""Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:"""
def safe_divide(numerator, denominator):
    #handle zero divison error
    try:
        # Convert both values to float (may raise ValueError)
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError()
        # if float(numerator):
        #     raise ValueError("Error: Please enter numeric values only.")
        result = numerator / denominator
        return f"The result of the divison is {result}"
        #return result
        #return float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only")
        

#testing function
#safe_divide("ten", 0)