file = open('input3.txt', "r") 
numbers = file.read().splitlines()
numbers = [list(i) for i in numbers]
file.close()


def split_array_oxygen(position, data):
	zeros = []
	ones = []
	for number in data:
		if number[position] == '1':
			ones.append(number)
		else:
			zeros.append(number)
	if len(zeros) <= len(ones):
		return ones
	else:
		return zeros

def split_array_co2(position, data):
	zeros = []
	ones = []
	for number in data:
		if number[position] == '1':
			ones.append(number)
		else:
			zeros.append(number)
	if len(zeros) <= len(ones):
		return zeros
	else:
		return ones

i = 0

oxygen = numbers
while len(oxygen) > 1:
	oxygen = split_array_oxygen(i, oxygen)
	i += 1

i = 0

co2 = numbers
while len(co2) > 1:
	co2 = split_array_co2(i, co2)
	i += 1

o = ''
c = ''

for i in oxygen[0]:
	o = o + i

for i in co2[0]:
	c = c + i

print(o)
print(c)
print(int(o,2) * int(c, 2))
