from functools import reduce
import itertools as it

with open('10.in', 'r') as puzzleInputFile:
    puzzleInput = list(puzzleInputFile.read().strip())

def lookAndSay(x):
    return ''.join(str(len(tuple(g))) + k for k, g in it.groupby(x))

print(len(reduce(lambda x, f: f(x), it.repeat(lookAndSay, 50), puzzleInput)))
