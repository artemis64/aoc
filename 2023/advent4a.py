file = open('input4.txt', 'r')
pointsTotal = 0 #variable for the final amount of points

for line in file:
    line = line.split() # split each line by space
    winNos = line[2:12]  # 0th item is 'Card', 1st item is noOfCard: - we don't care about those. Items 2-11 are winning numbers (it's different for the example!), 12th item is '|' 
    guessNos = line[13:] # 13th item til the end are the guess numbers (it's different for the example!)
    points = 0 # points we gain on this particular card
    for guess in guessNos: # we check each guess number if it's winning
        if guess in winNos and points == 0: # if the guess number is winning and it's the first winning one on the card
            points = 1 # we get 1 point
        elif guess in winNos: # if the guess number is winning but it's not the first one 
            points = 2*points # we double the number of points
    pointsTotal +=points # we add the number of points we gained on this card to the total sum of points
print(pointsTotal)