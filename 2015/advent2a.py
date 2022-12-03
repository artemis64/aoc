file = open('input2.txt', 'r')

paper = 0

for line in file:
	line = line.strip()
	dimensions = line.split('x')
	sides = [int(dimensions[0])*int(dimensions[1]), int(dimensions[0])*int(dimensions[2]), int(dimensions[2])*int(dimensions[1])]
	sides.sort()
	paper += 3*sides[0] + 2*sides[1] + 2*sides[2] 
print(paper)