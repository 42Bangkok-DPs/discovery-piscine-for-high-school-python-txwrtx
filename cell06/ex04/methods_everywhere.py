#!/usr/bin/env python3

import sys

def enlarge(text:str):
    text += "Z" * (8 - len(text))
    return text

def shrink(text:str):
    return text[slice(0, 8)]

if len(sys.argv) < 2: print("none")
else:
    for i in range(1, len(sys.argv)):
        current_text = sys.argv[i]

        if len(current_text) < 8:
            print(enlarge(current_text))
        elif len(current_text) > 8:
           print(shrink(current_text))
        else: print(current_text)
