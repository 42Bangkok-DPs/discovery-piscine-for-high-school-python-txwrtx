#!/usr/bin/env python3

def greetings(name=""):
    if name == "": name = "noble stranger"
    elif type(name) != str: return print("Error! It was not a name.")

    return print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
