file = open('input6.txt', "r") 
originalFish = file.readline().strip().split(",")
file.close()

fishNumbers = [0] * 9

for fish in originalFish:
	fishNumbers[int(fish)] +=1

zeroPosition = 0
children = 0

for i in range(256):
	zeroPosition = (zeroPosition + 1) % 7
	fishNumbers[(zeroPosition - 1) % 7] = fishNumbers[(zeroPosition - 1) % 7] + fishNumbers[7]
	fishNumbers[7] = fishNumbers[8]
	fishNumbers[8] = children
	children = fishNumbers[zeroPosition]

count = 0
for i in fishNumbers:
	count = count + i

	

print(count)
