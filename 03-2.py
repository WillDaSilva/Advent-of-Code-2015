with open('03.in', 'r') as puzzleInputFile:
    instructions = puzzleInputFile.read().strip()

directions = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
instructions = (directions[x] for x in instructions)
grid = dict()
grid[(0, 0)] = True
x1 = y1 = x2 = y2 = 0
for i in zip(*[instructions]*2):
    x1, y1, x2, y2 = x1 + i[0][0], y1 + i[0][1], x2 + i[1][0], y2 + i[1][1]
    grid[(x1, y1)] = grid[(x2, y2)] = True
print(sum(grid.values()))
