"""
Task Description:
You will create a script named finance_calculator.py. 
This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
"""
#variables
#user monthly income
monthly_income = float(input("Enter your monthly income: "))

#user monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

print("Your monthly savings are $", monthly_savings)
#calculate annual savings, assume a simple annual rate of 5%
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#display projected annual savings
print("Projected savings after one year, with interest, is: $", projected_annual_savings)