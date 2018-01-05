with open('19.in', 'r') as puzzleInputFile:
    puzzleInput = [x.strip() for x in puzzleInputFile.readlines()]

molecule = puzzleInput.pop()
replacements = (x.split(' => ') for x in puzzleInput[:-1])
molecules = set()
for key, replacement in replacements:
    start = 0
    while True:
        start = molecule.find(key, start)
        if start == -1:
            break
        end = start + len(replacement) - 2
        pieces = (molecule[:start], replacement, molecule[end:])
        molecules.add(''.join(pieces))
        start += 1
print(len(molecules))
