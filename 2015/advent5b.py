nice = 0

def checkDoubleDouble(SantaString):
	for i in range(len(SantaString)-1):
		if SantaString[i:i+2] in SantaString[:i] or SantaString[i:i+2] in SantaString[i+2:]:
			return True
	return False

def checkForDoubleWithSkip(SantaString):
	for i in range(len(SantaString)-2):
		if SantaString[i] == SantaString[i+2]:
			return True
	return False

file = open('input5.txt', 'r')

for line in file:
	line = line.strip()
	if checkForDoubleWithSkip(line):
		if checkDoubleDouble(line):
			nice +=1
print(nice)
	
