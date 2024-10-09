#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 3: print("none")
else : print(len(re.findall(r'\bthe\b', sys.argv[2])))
