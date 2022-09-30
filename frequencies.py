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


input = ['0', 4,4,'4','d','d','e',0,'a','d','4']
output = frequencies(input)
assert output['4'] == 4
assert output['d'] == 3
assert output['e'] == 1
assert output['a'] == 1
assert output['0'] == 2
assert 4 not in output.keys()
assert 0 not in output.keys()
