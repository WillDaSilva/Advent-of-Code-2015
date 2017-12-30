with open('05.in', 'r') as puzzleInputFile:
    puzzleInput = puzzleInputFile.readlines()

def hasThreeVowels(string):
    vowelCount = 0
    for character in string:
        vowelCount += character in 'aeiou'
        if vowelCount == 3:
            return True
    return False

def hasRepeatedLetter(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False

def hasNoBadSubString(string):
    return not any(x in string for x in ('ab', 'cd', 'pq', 'xy'))

niceRules = (hasThreeVowels, hasRepeatedLetter, hasNoBadSubString)
print(sum(all(rule(string) for rule in niceRules) for string in puzzleInput))
