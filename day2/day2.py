input = []
with open('input') as file:
    for line in file:
        entry = line.strip().split()
        input.append([
            entry[0].split('-'),
            entry[1].replace(':', ''),
            entry[2]
        ])

def verifyInput(min, max, letter, input):
    count = input.count(letter)
    if (count <= max) and (count >= min) :
        return True
    return False

def verifyTCP(pos1, pos2, letter, input):
    count = len(input)
    if ( ( input[pos1-1] == letter ) or ( input[pos2-1] == letter ) ) and ( input[pos1-1] != input[pos2-1] ) :
        return True
    return False

countA = 0
countB = 0
for password in input:
    if verifyInput(int(password[0][0]), int(password[0][1]), password[1], password[2]):
        countA+=1
    if verifyTCP(int(password[0][0]), int(password[0][1]), password[1], password[2]):
        countB+=1

print(countA)
print(countB)
