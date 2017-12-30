from functools import reduce
import itertools as it
from operator import mul

with open('02.in', 'r') as puzzleInputFile:
    dimensions = puzzleInputFile.readlines()

dimensions = (sorted(int(y) for y in x.split('x')) for x in dimensions)
dimensions = (reduce(mul, y) for x in dimensions for y in it.combinations(x, 2))
print(sum(3 * x[0] + 2 * (x[1] + x[2]) for x in zip(*[dimensions]*3)))
