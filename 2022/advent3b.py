def getLetterScore(letter):
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return (alphabet.index(letter) + 1)

file = open('input3.txt', 'r')

priority = 0

while file:
	first = file.readline().strip()
	if first == '':
		break
	second = file.readline().strip()
	third = file.readline().strip()
	firstAndSecond = []
	for thingy in first:
		if thingy in second:
			firstAndSecond.append(thingy)
	for thingy in firstAndSecond:
		if thingy in third:
			badge = thingy
			break
	priority += getLetterScore(badge)

	
print(priority)