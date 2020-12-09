TARGET = 2020

input = []
with open('input') as file:
    for line in file:
        input.append(int(line.strip()))

def findSumElements(input, target):
    for n in input:
        expected = target - n
        if expected in input:
            return (n, expected)
    return None

# PART 1

result = findSumElements(input, TARGET)
print(result, " : ", (result[0] * result[1]))

# PART 2

for n in input:
    expected = TARGET - n
    restSum = findSumElements(input, expected)
    if restSum is not None:
        print(n, restSum, " : ", n * restSum[0] * restSum[1])
        break