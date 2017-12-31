import itertools as it

with open('09.in', 'r') as puzzleInputFile:
    distances = (x.strip().split(' = ') for x in puzzleInputFile.readlines())

def pairs(x):
    a, b = it.tee(x)
    next(b, None)
    return zip(a, b)

distances = ((tuple(sorted(x[0].split(' to '))), int(x[1])) for x in distances)
distances = dict(distances)
places = {x for y in distances for x in y}
routeLength = lambda x: sum(distances[tuple(sorted(y))] for y in pairs(x))
print(min(routeLength(route) for route in it.permutations(places)))
