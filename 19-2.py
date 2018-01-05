from random import shuffle

with open('19.in', 'r') as puzzleInputFile:
    puzzleInput = [x.strip() for x in puzzleInputFile.readlines()]

molecule = original = puzzleInput.pop()
replacements = [tuple(x.split(' => ')) for x in puzzleInput]
replacements = sorted(replacements[:-1], key=lambda x: len(x[1]))
steps = 0
while molecule != 'e':
    lastMolecule = molecule
    for key, replacement in replacements:
        steps += replacement in molecule
        molecule = molecule.replace(replacement, key, 1)
    if molecule == lastMolecule:
        shuffle(replacements)
        molecule = original
        steps = 0
print(steps)
