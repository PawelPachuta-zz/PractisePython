# Program is printing out user age and saying when they will turn  100

from datetime import datetime, timedelta

print("Give my your name and age and I will tell which year you will turn 100!")
b = input("name: ")
a = int(input("age: " )) * 365
today = datetime.now()
hundred_years_old = today + timedelta(days=36500 - a)
exactly_date = datetime.strftime(hundred_years_old, '%Y')

print(exactly_date)
