def getLetterScore(letter):
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return (alphabet.index(letter) + 1)

file = open('input3.txt', 'r')

priority = 0

for line in file:
	line = line.strip()
	first = line[:(int(len(line)/2))]
	second = line[(int(len(line)/2)):]
	for thingy in first:
		if (thingy in second):
			priority += getLetterScore(thingy)
			break
print(priority)
