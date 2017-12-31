from copy import deepcopy
import operator as op

with open('07.in', 'r') as puzzleInputFile:
    instructions = puzzleInputFile.readlines()

instructions = (x.strip().split(' -> ') for x in instructions)
instructions = ((x[0].split(), x[1]) for x in instructions)
wires = {wire:source for source, wire in instructions}

def resolve(wire):
    def getSignal(x, flag=None):
        try:
            return int(x)
        except ValueError:
            return resolve(x)
    target = wires[wire]
    if type(target) == int:
        signal = target
    elif len(target) == 1:
        signal = getSignal(target[0])
    elif len(target) == 2:
        if target[0] == 'NOT': operation = op.inv
        signal = operation(getSignal(target[1]))
    elif len(target) == 3:
        if target[1] == 'AND': operation = op.and_
        elif target[1] == 'OR': operation = op.or_
        elif target[1] == 'LSHIFT': operation = op.lshift
        elif target[1] == 'RSHIFT': operation = op.rshift
        signal = operation(getSignal(target[0]), getSignal(target[2]))
    wires[wire] = 0xFFFF & signal
    return wires[wire]

wiresCopy = deepcopy(wires)
newB = resolve('a')
wires = wiresCopy
wires['b'] = newB
print(resolve('a'))
