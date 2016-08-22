#!/usr/bin/env python
"""Reads the source file and separates code examples"""
import sys
from extractor import Code

if len(argv[])>1:
    filename = argv[1]
else
    filename = "Codes.txt"
SEPARATOR = "-----"


with open("Codes.txt", "r") as source:
    instance = ""
    for line in source:
        # This will hold the current code

        stripped = line.rstrip().split()
        # We can check code separator only if the line is not empty
        if stripped != []:
            if stripped[0] != SEPARATOR:
                instance += line
            else:
                # print(instance)
                code = Code(instance)
                code.run()
                print(code)
                instance = ""
