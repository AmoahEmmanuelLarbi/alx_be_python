"""
Task Description:

Develop a script named daily_reminder.py. 
This script will ask the user for a single task, its priority level, and if it is time-sensitive. 
The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.
"""
#solution
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()

#using match case to make decision
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. You must complete before the deadline")
    case "medium":
        print(f"Note: '{task}' is a {priority} priority task.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
    case _:
        print("Your task priority wasn't specified")
