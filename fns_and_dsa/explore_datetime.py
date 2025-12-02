from datetime import datetime, timedelta
"""
Task Instructions:
Your task is to create a Python script named explore_datetime.py. 
This script will demonstrate your ability to use the datetime module for handling dates and times in Python.
"""
"""
Task 1:
Create a function with a name display_current_datetime and
save the current date inside a current_date variable
"""

# create function
def display_current_datetime():
    current_date = datetime.now()
    return current_date

#
# print(display_current_datetime())
#format date to readable text
print(f"Current date and time: {display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")}")

#Task 2
def calculate_future_date(days_to_added):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_added)
    return future_date.strftime("%Y-%m-%d")
    

number_of_days = int(input("Enter number of days to add to the current date: "))
print(calculate_future_date(number_of_days))
