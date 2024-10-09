#!/usr/bin/env python3
f_num = int(input("Enter the first number:\n"))
s_num = int(input("Enter the second number:\n"))

result = f_num * s_num

print(f"{f_num} x {s_num} = {result}")

if result > 0: print("The result is positive.")
elif result < 0: print("The result is negative.")
else: print("The result is positive and negative.")
