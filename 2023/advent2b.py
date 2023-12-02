file = open('input2.txt', 'r')
summa = 0 # variable for the final sum

for line in file:
    line = line.split()
    line.pop(0)
    line.pop(0)

    rgbMax = [0,0,0] # we will be checking for the maximum amount of cubes in each color
    for i in range(len(line) // 2):
        if line[2*i+1][0] == 'r' and int(line[2*i]) > rgbMax[0]: # if the cubes are red and it's more of them than the current red maximum
            rgbMax[0] = int(line[2*i]) # we change the maximum
        elif line[2*i+1][0] == 'g' and int(line[2*i]) > rgbMax[1]:
            rgbMax[1] = int(line[2*i])
        elif line[2*i+1][0] == 'b' and int(line[2*i]) > rgbMax[2]:
            rgbMax[2] = int(line[2*i])
    summa += rgbMax[0]*rgbMax[1]*rgbMax[2] # add to the sum the color maximums multiplied together
print(summa)

