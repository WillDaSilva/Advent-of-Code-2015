from functools import reduce
import itertools as it
from operator import mul

with open('15.in', 'r') as puzzleInputFile:
    ingredients = (x.strip().split() for x in puzzleInputFile.readlines())

def compositions(n, width):
    for c in it.combinations(range(n + width - 1), width - 1):
        z = zip(it.chain((-1,), c), it.chain(c + (n + width - 1,)))
        yield tuple(y - x - 1 for x, y in z)

indexes = (2, 4, 6, 8)
extract = lambda x: tuple(int(x[i].strip(',')) for i in indexes)
ingredients = tuple(extract(x) for x in ingredients)
n = len(ingredients)
best = 0
for x in compositions(100, n):
    qualities = zip(*(tuple(a*x[i] for a in ingredients[i]) for i in range(n)))
    qualities = (sum(quality) for quality in qualities)
    score = reduce(mul, (q if q > 0 else 0 for q in qualities))
    if score > best:
        best = score
print(best)
