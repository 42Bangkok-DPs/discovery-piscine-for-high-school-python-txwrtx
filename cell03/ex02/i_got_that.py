#!/usr/bin/env python3
text = "-1"

while True :
    if text == "-1": text = str(input("What you gotta say? : "))
    else : text = str(input("I got that! Anything else? : "))

    if text == "STOP" :break;
