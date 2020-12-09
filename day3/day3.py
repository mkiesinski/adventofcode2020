input = []
with open('input') as file:
    for line in file:
        input.append(line.strip())

def countTreesDiagonal(right, down, input, currentPos = (0,0), count = 0):
    nextPos = (currentPos[0] + right, currentPos[1] + down)
    if nextPos[1] >= len(input):
        return count

    lineLength = len(input[nextPos[1]])

    if input[nextPos[1]][nextPos[0] % lineLength] == '#':
        count+=1

    return countTreesDiagonal(right, down, input, nextPos, count)

# part 1
print(countTreesDiagonal(3,1,input))

#part 2
result = countTreesDiagonal(1,1,input) * countTreesDiagonal(3,1,input) * countTreesDiagonal(5,1,input) * countTreesDiagonal(7,1,input) * countTreesDiagonal(1,2,input)
print(result)