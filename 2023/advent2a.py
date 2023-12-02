file = open('input2.txt', 'r')
gameNo = 1  # game count so we don t have to parse it
summa = 0 # variable for the final sum

for line in file: # checking each line separately
    line = line.split() # splitting the line by the space
    line.pop(0) # getting rid of the first item in line which is "Game"
    line.pop(0) # getting rid of the first item in line which is now the number of the game - we store it in gameNo variable instead

    possible = True # at the beginning we take that this game is possible
    for i in range(len(line) // 2): # in our line list we have always at the position 2k the number of the cubes and at 2k+1 their color - so we check per each pair of items in line  
        if line[2*i+1][0] == 'r' and int(line[2*i]) > 12: # if cubes are red and it's more of them than 12 the game is not possible 
            possible = False # we change to not possible
            break # and break out of the loop because it's enough if it's not possible once - we don't have to check more times
        elif line[2*i+1][0] == 'g' and int(line[2*i]) > 13:
            possible = False
            break
        elif line[2*i+1][0] == 'b' and int(line[2*i]) > 14:
            possible = False
            break
    if possible: # if the game is possible
        summa += gameNo # we add it's ID to the total sum
    gameNo +=1 # increase the game count
print(summa)