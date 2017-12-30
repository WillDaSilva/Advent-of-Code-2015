from hashlib import md5

with open('04.in', 'r') as puzzleInputFile:
    key = puzzleInputFile.read().strip()

i = 1
while md5((key + str(i)).encode('utf-8')).hexdigest()[:6] != '000000': i += 1
print(i)
