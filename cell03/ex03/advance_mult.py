#!/usr/bin/env python3
row = 0
column = 0

while row < 11:
    print(f"Table de {row}:", end=" ")
    while column < 11:
        print(row * column, end=" ")
        column += 1
    row += 1
    column = 0
    print()
