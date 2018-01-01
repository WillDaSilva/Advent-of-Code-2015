with open('11.in', 'r') as puzzleInputFile:
    password = puzzleInputFile.read().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
pairs = [letter + letter for letter in alphabet]
inc3 = [''.join(x) for x in zip(alphabet[:-2], alphabet[1:-1], alphabet[2:])]

def nextPassword(password):
    password = password[:-1] + chr(ord(password[-1]) + 1)
    while chr(ord('z') + 1) in password:
        i = password.index(chr(ord('z') + 1))
        password = ''.join((
            password[:i-1],
            chr(ord(password[i-1]) + 1),
            'a',
            password[i+1:]
        ))
    for c in 'ilo':
        i = password.find(c)
        if i != -1:
            password = ''.join((password[:i], chr(ord(c) + 1), 'a' * (8-i-1)))
            break
    return password

def isValid(password):
    if not any(trio in password for trio in inc3):
        return False
    numPairs = 0
    for pair in pairs:
        numPairs += pair in password
        if numPairs == 2:
            return True
    return False

def nextValidPassword(password):
    while not isValid(password):
        password = nextPassword(password)
    return password

print(nextValidPassword(password))
