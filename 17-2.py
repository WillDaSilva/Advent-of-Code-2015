from copy import copy
import itertools as it

with open('17.in', 'r') as puzzleInputFile:
    containers = list(int(x) for x in puzzleInputFile.readlines())

def fit(n, containers, used):
    for i in range(len(containers)):
        if containers[i] <= n:
            used.append(containers[i])
            yield from fit(n - containers[i], containers[i + 1:], copy(used))
            used.pop()
    if n == 0:
        yield used

combinations = list(fit(150, sorted(containers, reverse=True), []))
least = min(len(x) for x in combinations)
print(sum(len(x) == least for x in combinations))
