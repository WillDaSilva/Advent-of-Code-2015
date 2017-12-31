with open('08.in', 'r') as puzzleInputFile:
    strings = (x.strip() for x in puzzleInputFile.readlines())

print(sum(x.count('\\') + x.count('"') + 2 for x in strings))
