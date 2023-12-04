file = open('input4.txt', 'r')
cardDetails = [] # we store card details in here - there will be one list with three items per card. 0th item is list of it's winning numbers, 1st item in the list is the list of the guesses for the card, 2nd item is the number of the cards we have (original + copies)
cardsAmount = 0 #total amount of cards we have

for line in file:
    line = line.split()
    cardDetails.append([line[2:12], line[13:], 1]) # for each card we append winning numbers, guesses and at the beginning we have just 1 original of each card

for cardNo, card in enumerate(cardDetails): # we check each card + note the card number (it's 1 lower than in the input - Card 1 is my card number 0 etc.)
    wins = 0 # number of wins so far on this card
    for guess in card[1]: # we check for each guess 
        if guess in card[0]: # if the guess number is also a winning number
            wins +=1 # we add a win
            cardDetails[cardNo + wins][2] +=card[2] # to the card that is current amount of wins after current card we add a copy for each instance of the current card
    cardsAmount += card[2] # after we check everything for the current card we add the number of instances we own of it to the total sum
print(cardDetails)
print(cardsAmount)