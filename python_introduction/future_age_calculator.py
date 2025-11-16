"""
Create a Python script that asks the user for their current age and then 
calculates how old they will be in a specific future year
"""

#variable to store user age
#prompt for user current age
user_current_age = int(input("How old are you? "))

#user age in 2050
future_age = user_current_age + 27
print(f"In 2050, you will be {future_age} years old.")
