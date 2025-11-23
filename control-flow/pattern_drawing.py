"""
Task Description:

Develop a Python script named pattern_drawing.py. 
This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
"""
#solution
pattern = int(input("Enter the size of the pattern: "))

counter = 0
#outer loop
while counter < pattern:
    #inner loop
    for item in range(pattern):
        print("*", end = "")
    counter += 1
    print()