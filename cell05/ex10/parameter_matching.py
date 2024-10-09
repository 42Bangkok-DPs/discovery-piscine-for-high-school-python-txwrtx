#!/usr/bin/env python3
import sys

if len(sys.argv) < 2: print("none")
else :     
    text = str(input("What was the parameter? "))
    if text == sys.argv[1]: print("Good job!")
    else: print("Nope, sorry...")
