with open('03.in', 'r') as puzzleInputFile:
    instructions = puzzleInputFile.read().strip()

directions = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
instructions = (directions[x] for x in instructions)
grid = dict()
grid[(0, 0)] = True
x = y = 0
for i in instructions:
    x, y = x + i[0], y + i[1]
    grid[(x, y)] = True
print(sum(grid.values()))
