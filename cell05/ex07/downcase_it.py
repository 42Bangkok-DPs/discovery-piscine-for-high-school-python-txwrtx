#!/usr/bin/env python3
import sys

try:
    print(sys.argv[1].lower())
except IndexError :
    print("none")
