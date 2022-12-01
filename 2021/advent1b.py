file = open('input1.txt', "r") 
numbers = file.read().splitlines()
numbers = [int(i) for i in numbers]
file.close()

count = 0

for i in range(len(numbers)-3):
	if numbers[i] < numbers[i+3]:
		count += 1

print("In total increased {} times".format(count))