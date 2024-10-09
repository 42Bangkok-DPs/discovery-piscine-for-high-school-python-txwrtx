#!/usr/bin/env python3

def find_the_redheads(dic:dict):
    result = []
    for key, value in dic.items():
        if value == "red": result.append(key)
    return result

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))
