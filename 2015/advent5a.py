nice = 0
vowels = 'aeiou'
prohibited = ['ab', 'cd', 'pq', 'xy']

def checkForVowels(SantaString):
	vowelCount = 0
	for letter in SantaString:
		if letter in vowels:
			vowelCount +=1
			if vowelCount == 3:
				return True
	return False

def checkForDoubles(SantaString):
	previous = SantaString[0]
	for i in range(1,len(SantaString)):
		if previous == SantaString[i]:
			return True
		previous = SantaString[i]
	return False

def deosntContainProhibited(SantaString):
	for proh in prohibited:
		if proh in SantaString:
			return False
	return True

file = open('input5.txt', 'r')

for line in file:
	line = line.strip()
	
	if deosntContainProhibited(line):
		if checkForDoubles(line):
			if checkForVowels(line):
				nice +=1
print(nice)