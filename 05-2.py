with open('05.in', 'r') as puzzleInputFile:
    puzzleInput = puzzleInputFile.readlines()

def hasDuplicatePair(string):
    return any(string.count(string[i:i+2]) > 1 for i in range(len(string) - 2))

def hasSandwich(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False

niceRules = (hasSandwich, hasDuplicatePair)
print(sum(all(rule(string) for rule in niceRules) for string in puzzleInput))
