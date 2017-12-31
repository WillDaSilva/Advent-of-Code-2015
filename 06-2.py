import numpy as np

with open('06.in', 'r') as puzzleInputFile:
    instructions = puzzleInputFile.readlines()

def extractRect(rectText):
    return tuple(int(x) for x in rectText.replace(' through ', ',').split(','))

grid = np.zeros((1000, 1000), dtype=int)
for instruction in instructions:
    if instruction.startswith('turn on '):
        x1, y1, x2, y2 = extractRect(instruction[len('turn on '):])
        grid[x1:x2+1, y1:y2+1] += 1
    elif instruction.startswith('turn off '):
        x1, y1, x2, y2 = extractRect(instruction[len('turn off '):])
        grid[x1:x2+1, y1:y2+1] = np.clip(grid[x1:x2+1, y1:y2+1] - 1, 0, None)
    elif instruction.startswith('toggle '):
        x1, y1, x2, y2 = extractRect(instruction[len('toggle '):])
        grid[x1:x2+1, y1:y2+1] += 2
print(np.sum(grid))
