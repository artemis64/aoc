file = open('input10.txt', 'r')
chunks = []
for line in file:
	chunks.append(line.strip())
file.close()

opened = ["(", "[", "{", "<"]
closed = [")", "]", "}", ">"]
scores = [1, 2, 3, 4]
scores2 = [3, 57, 1197, 25137]
score = []
count = 0
delete = []
print(len(chunks))
for line in range(len(chunks)):
	remainToClose = []
	for char in chunks[line]:
		if char in opened:
			remainToClose.append(char)
		elif char in closed:
			if len(remainToClose) > 0 and opened.index(remainToClose[-1]) == closed.index(char):
				remainToClose.pop()
			else:
				count = count + scores2[closed.index(char)]
				delete.append(line)
				break
print(len(chunks))
print(count)
print(len(delete))
delete.sort()
while len(delete) > 0:
	del chunks[delete.pop()]

print(len(chunks))
for line in chunks:
	remainToClose = []
	s = 0
	for char in line:
		if char in opened:
			remainToClose.append(char)
		elif char in closed:
			if opened.index(remainToClose[-1]) == closed.index(char):
				remainToClose.pop()
	while len(remainToClose) > 0:
		#print("s {} closing {}".format(s, remainToClose[-1]))
		s = s * 5 + scores[opened.index(remainToClose.pop())]
	score.append(s)

score.sort()

print(len(score))
print(score[len(score)/2])

