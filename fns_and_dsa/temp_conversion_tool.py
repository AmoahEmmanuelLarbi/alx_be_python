"""
Create a Python script named temp_conversion_tool.py. 
This script will define functions to convert temperatures between Celsius and Fahrenheit, 
demonstrating the use of global variables to store conversion factors that are accessible within functions.
"""
#GLOBAL VARIABLES
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implementation
#functions
#converting fahrenheit to celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

#converting celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

convert_to_celsius(100)
print(convert_to_fahrenheit(0))
print(convert_to_celsius(100))

#prompt user to enter temperature
temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if unit == "f":
    result = convert_to_celsius(temperature)
    print(f"{temperature} F is {result} C")
elif unit == "c":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature} C is {result} F")
else:
    print("Temperature unit is invalid")
