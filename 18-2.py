import numpy as np

states = {'#': True, '.': False}
with open('18.in', 'r') as puzzleInputFile:
    grid = [[states[y] for y in x.strip()] for x in puzzleInputFile]

adjacents = tuple((x,y) for x in (-1,0,1) for y in (-1,0,1) if not x == y == 0)
def sumAdjacents(x, y, grid):
    total = 0
    for u, v in ((x + i, y + j) for i, j in adjacents):
        if u >= 0 and u < grid.shape[0] and v >= 0 and v < grid.shape[1]:
            total += grid[u, v]
    return total

def advance(a, b):
    for x, y in np.ndindex(*a.shape):
        adjSum = sumAdjacents(x, y, a)
        b[x, y] = a[x, y] and adjSum in (2, 3) or adjSum == 3
    b[::b.shape[0]-1, ::b.shape[1]-1] = True
    return b

a = np.asarray(grid, dtype=int)
a[::a.shape[0]-1, ::a.shape[1]-1] = True
b = np.empty_like(a)
for _ in range(100 // 2):
    b = advance(a, b)
    a = advance(b, a)
print(np.sum(a))
