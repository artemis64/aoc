file = open('input2.txt', 'r')

ribbon = 0

for line in file:
	line = line.strip()
	dimensions = line.split('x')
	dimensions = [ int(x) for x in dimensions ]
	dimensions.sort()
	ribbon += 2*dimensions[0] + 2*dimensions[1] + dimensions[0]*dimensions[1]*dimensions[2]
	
print(ribbon)