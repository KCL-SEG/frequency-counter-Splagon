"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for element in items:
        element = str(element)
        if element in frequencies.keys():
            frequencies[element] = frequencies.get(element) + 1;
        else:
            frequencies[element] = 1;
        print(frequencies)
    return frequencies
