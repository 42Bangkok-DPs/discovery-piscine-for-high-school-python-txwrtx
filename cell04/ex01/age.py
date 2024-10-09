#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
next_ten_years = 10

print(f"You are currently {age} years old.")

while next_ten_years <= 30:
    print(f"In {next_ten_years} years, you'll be {age + next_ten_years} years old.")
    next_ten_years += 10
