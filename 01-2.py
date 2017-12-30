with open('01.in', 'r') as puzzleInputFile:
    puzzleInput = puzzleInputFile.read().strip()

level = 0
for i, x in enumerate(puzzleInput):
    level += {'(': 1, ')': -1}[x]
    if level < 0:
        print(i + 1)
        break
