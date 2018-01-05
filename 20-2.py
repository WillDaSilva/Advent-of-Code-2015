import itertools as it
import toolkit as tk # https://github.com/WillDaSilva/python-toolkit

with open('20.in', 'r') as puzzleInputFile:
    puzzleInput = int(puzzleInputFile.read())

factors = ((tk.factor(x), x) for x in it.count(10**5, 10))
validFactors = (((z for z in x if y // z <= 50), y) for x, y in factors)
print(tk.first_true(validFactors, lambda x: sum(x[0]) * 11 > puzzleInput)[1])
