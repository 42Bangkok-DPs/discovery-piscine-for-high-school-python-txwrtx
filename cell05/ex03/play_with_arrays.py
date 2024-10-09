#!/usr/bin/env python3
num_list = [2, 8, 9, 48, 8, 22, -12, 2]
result = set()

print(num_list)

for i in num_list:
    if i >= 5 and i + 2 not in result:
        result.add(i + 2)

print(result)
