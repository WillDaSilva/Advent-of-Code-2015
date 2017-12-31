from ast import literal_eval

with open('08.in', 'r') as puzzleInputFile:
    strings = (x.strip() for x in puzzleInputFile.readlines())

print(sum(len(x) - len(literal_eval(x)) for x in strings))
