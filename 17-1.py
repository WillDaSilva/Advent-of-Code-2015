import itertools as it

with open('17.in', 'r') as puzzleInputFile:
    containers = (int(x) for x in puzzleInputFile.readlines())

def fit(n, containers):
    for i in range(len(containers)):
        if containers[i] <= n:
            yield from fit(n - containers[i], containers[i + 1:])
    if n == 0:
        yield True

print(sum(fit(150, sorted(containers, reverse=True))))
