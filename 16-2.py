from operator import gt, lt, eq

with open('16.in', 'r') as puzzleInputFile:
    sues = (x.strip().split()[1:] for x in puzzleInputFile.readlines())

def retriveInt(x):
    try:
        return int(x)
    except ValueError:
        return x

sues = (tuple(retriveInt(y.strip(':,')) for y in x) for x in sues)
sues = {x[0]: dict(zip(*[iter(x[1:])]*2)) for x in sues}

data = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

comparators = { # Only contains non-standard (eq) comparators
    'cats': gt,
    'trees': gt,
    'pomeranians': lt,
    'goldfish': lt
}

for i, sue in sues.items():
    keyIntersection = sue.keys() & data.keys()
    if all(comparators.get(k, eq)(sue[k], data[k]) for k in keyIntersection):
        print(i)
        break
