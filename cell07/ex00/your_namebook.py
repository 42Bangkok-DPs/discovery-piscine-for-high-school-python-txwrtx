#!/usr/bin/env python3

def array_of_names(dic:dict):
    result = []
    for key, value in dic.items():
        result.append(f"{key.capitalize()} {value.capitalize()}")
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
