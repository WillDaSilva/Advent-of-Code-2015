import json

with open('12.in', 'r') as puzzleInputFile:
    puzzleInput = json.load(puzzleInputFile)

def parse(struct):
    total = 0
    if not ('red' in struct and type(struct) == type(dict().values())):
        for x in struct:
            if type(x) == int:
                total += x
            elif type(x) == dict:
                total += parse(x.values())
            elif type(x) == list:
                total += parse(x)
    return total

print(parse(puzzleInput.values()))
