"""
Task Description:
Create a Python script named multiplication_table.py. 
This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.
"""

#solution
number = int(input("Enter a number to see its multiplication table: "))

#for loop to calculate product
for value in range(1, 11):
    print(f"{number} * {value} = {number*value}")