with open('01.in', 'r') as puzzleInputFile:
    puzzleInput = puzzleInputFile.read().strip()

print(sum({'(': 1, ')': -1}[x] for x in puzzleInput))
