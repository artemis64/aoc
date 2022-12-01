file = open('input3.txt', "r") 
numbers = file.read().splitlines()
#numbers = [int(i,2) for i in numbers]
numbers = [list(i) for i in numbers]
file.close()

amounts = [0] * len(numbers[0])

for cislo in numbers:
	i = 0
	for cifra in cislo:
		if cifra == '1':
			amounts[i] += 1
		i += 1

gamma = ''
epsilon = ''

for i in amounts:
	if i > len(numbers)/2:
		gamma = gamma + '1'
		epsilon = epsilon + '0'
	else:
		gamma = gamma + '0'
		epsilon = epsilon +'1'

print(amounts)
print(gamma)
print(epsilon)
print(int(gamma,2) * int(epsilon, 2))
