#!/usr/bin/env python3
num = float(input("Give me a number : "))

decimal = num - int(num)

if not decimal: print("This number is an integer.")
else: print("This number is decimal.")
