"""
Task Description:
Create a Python script named weather_advice.py. 
This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. 
This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.
"""

prompt = input("What's the weather like today? (sunny/rainy/cold): ").lower()
recommendation_text = ""

#using if, elif and else to provide recommendations
if prompt == "sunny":
    recommendation_text = "Wear a t-shirt and sunglasses."
elif prompt == "rainy":
    recommendation_text = "Don't forget your umbrella and a raincoat."
elif prompt == "cold":
    recommendation_text = "Make sure to wear a warm coat and a scarf."
else:
    recommendation_text = "Sorry, I don't have recommendations for this weather."

#display recommendation
print(recommendation_text)