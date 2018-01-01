import itertools as it
from math import factorial

def pairwise(x):
    a, b = it.tee(x)
    next(b, None)
    return zip(a, b)

with open('13.in', 'r') as puzzleInputFile:
    relations = puzzleInputFile.readlines()

sign = {'gain': 1, 'lose': -1}
relations = (x.strip('\n.').split() for x in relations)
relations = {(x[0], x[10]): sign[x[2]] * int(x[3]) for x in relations}
names = {x[0] for x in relations}
seatings = it.islice(it.permutations(names), factorial(len(names) - 1))
edgeScores = lambda x: relations[(x[0], x[-1])] + relations[(x[-1], x[0])]
score = lambda seating: sum(relations[x] for x in pairwise(seating))
print(max(score(x) + score(reversed(x)) + edgeScores(x) for x in seatings))
