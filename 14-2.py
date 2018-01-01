with open('14.in', 'r') as puzzleInputFile:
    reindeer = (x.strip() for x in puzzleInputFile.readlines())

# (rest, fly, speed, [state, ticks, distance, score])
stats = lambda x: (int(x[13]), int(x[6]), int(x[3]),
                   [1, int(x[6]), int(x[3]), 0])
reindeer = [stats(x.split()) for x in reindeer]
maxDist = max(reindeer, key=lambda x: x[3][2])[3][2]
for _ in range(2503):
    for x in reindeer:
        x[3][3] += x[3][2] == maxDist
    for x in reindeer:
        x[3][1] -= 1 # tick
        if not x[3][1]: # if ticks == 0: change state
            x[3][0] = not x[3][0]
            x[3][1] = x[x[3][0]]
        if x[3][0]: # if flying: move
            x[3][2] += x[2]
        if x[3][2] > maxDist:
            maxDist = x[3][2]
print(max(reindeer, key=lambda x: x[3][3])[3][3])
