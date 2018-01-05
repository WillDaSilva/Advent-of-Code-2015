import itertools as it

weapons = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))
armourItems = ((0, 0, 0), (13, 0, 1), (31, 0, 2),
               (53, 0, 3), (75, 0, 4), (102, 0, 5))
rings = ((0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0),
         (20, 0, 1), (40, 0, 2), (80, 0, 3))

with open('21.in', 'r') as puzzleInputFile:
    bossStats = tuple(int(x.split()[-1]) for x in puzzleInputFile.readlines())

cda = it.product(weapons, armourItems, rings, rings)
cda = (zip(*x) for x in cda if (0, 0, 0) in (x[2], x[3]) or x[2] != x[3])
cda = ([sum(y) for y in x] for x in cda)
for cost, damage, armour in sorted(cda, key=lambda x: x[0]):
    health = 100
    bossHealth, bossDamage, bossArmour = bossStats
    while bossHealth > 0 and health > 0:
        bossHealth -= 1 if damage - bossArmour <= 0 else damage - bossArmour
        health -= 1 if bossDamage - armour <= 0 else bossDamage - armour
    if bossHealth <= 0:
        break
print(cost)
