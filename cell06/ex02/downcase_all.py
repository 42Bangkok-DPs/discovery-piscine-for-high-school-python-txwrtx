#!/usr/bin/env python3

import sys

if len(sys.argv) < 2: print("none")
else: 
    for i in range(1, len(sys.argv)):
        print(sys.argv[i].lower())
