file = open('input14.txt', 'r')
polymer = ''
mapa = {}
for line in file:
	thisLine = line.strip()
	if '->' in thisLine:
		mapa[thisLine[:2]] = thisLine[-1]
	elif thisLine != '':
		polymer = thisLine
file.close()

pairs = {}
counts = {}

for i in range(len(polymer)-1):
	if polymer[i:i+2] in pairs:
		pairs[polymer[i:i+2]] +=1
	else:
		pairs[polymer[i:i+2]] =1

for i in polymer:
	if i in counts:
		counts[i] +=1
	else:
		counts[i] = 1

for step in range(40):
	for key, value in pairs.copy().items():
		link = mapa[key]
		pairs[key] -= value
		if key[0] + link in pairs:
			pairs[key[0] + link] += value
		else:
			pairs[key[0] + link] = value
		if link + key[1] in pairs:
			pairs[link + key[1]] += value
		else:
			pairs[link + key[1]] = value
		if link in counts:
			counts[link] += value
		else:
			counts[link] = value

print(max(counts.values()) - min(counts.values()))
