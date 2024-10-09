#!/usr/bin/env python3
import sys

result = []

if len(sys.argv) < 2: print("none")
else:
    result = list(range(int(sys.argv[1]), int(sys.argv[2]) + 1))
    print(result)
