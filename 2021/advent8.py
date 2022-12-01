class Case:
  def __init__(self, array):
  	self.digits = array[0]
  	self.numbers = array[1]
cases = []
file = open('input8.txt', 'r')
for line in file:
	case = line.strip().split(" | ")
	if len(case) > 1:
		cases.append(Case(case))
file.close()

count = 0
for case in cases:
	case.digits = case.digits.strip().split()
	case.numbers = case.numbers.strip().split()
	for i in case.numbers:
		if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
			count +=1
summa = 0
for case in cases:
	schema = [0] * 7
	cifry = [0] * 10
	petky = []
	sestky = []
	for i in case.digits:
		if len(i) == 2:
			cifry[1] = i
		elif len(i) == 3:
			cifry[7] = i
		elif len(i) == 4:
			cifry[4] = i
		elif len(i) == 7:
			cifry[8] = i
		elif len(i) == 5:
			petky.append(i)
		else:
			sestky.append(i)


	for i in cifry[7]:
		if i not in cifry[1]:
			schema[0] = i
			break
	

	for pet in petky:
		if cifry[1][0] in pet and cifry[1][1] in pet:
			cifry[3] = pet
			petky.remove(pet)
			break

	for i in cifry[8]:
		if i not in cifry[3] and i in cifry[4]:
			schema[1] = i
		elif i not in cifry[3] and i not in cifry[4]:
			schema[4] = i

	for sest in sestky:
		if cifry[1][0] in sest and cifry[1][1] in sest and schema[1] in sest and schema[4] in sest:
			cifry[0] = sest
			sestky.remove(sest)
			break

	for i in cifry[8]:
		if i not in cifry[0]:
			schema[3] = i
			break

	for i in cifry[0]:
		if i not in (cifry[1] + schema[0] + schema[1] + schema[4]):
			schema[6] = i
			break

	for sest in sestky:
		if schema[4] in sest:
			cifry[6] = sest
		else:
			cifry[9] = sest

	for i in cifry[1]:
		if i not in cifry[6]:
			schema[2] = i
		else:
			schema[5] = i

	for pet in petky:
		if schema[1] in pet:
			cifry[5] = pet
		else:
			cifry[2] = pet
	
	for i in range(len(cifry)):
		cifry[i] = sorted(cifry[i])

	print(cifry)
	print(sorted(case.numbers[3]))
	temp = 0
	temp = temp + cifry.index(sorted(case.numbers[0]))*1000
	temp = temp + cifry.index(sorted(case.numbers[1]))*100
	temp = temp + cifry.index(sorted(case.numbers[2]))*10
	temp = temp + cifry.index(sorted(case.numbers[3]))
	summa = summa + temp

print(summa)





