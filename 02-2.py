from functools import reduce
import itertools as it
from operator import mul

with open('02.in', 'r') as puzzleInputFile:
    dimensions = puzzleInputFile.readlines()

dimensions = (sorted(int(y) for y in x.split('x')) for x in dimensions)
print(sum(2 * (x[0] + x[1]) + reduce(mul, x) for x in dimensions))
