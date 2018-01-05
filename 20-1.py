import itertools as it
import toolkit as tk # https://github.com/WillDaSilva/python-toolkit

with open('20.in', 'r') as puzzleInputFile:
    puzzleInput = int(puzzleInputFile.read())

sumFactors = ((sum(tk.factor(x)), x) for x in it.count(10**5, 10))
print(tk.first_true(sumFactors, lambda x: x[0] * 10 > puzzleInput)[1])
