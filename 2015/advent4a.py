def getTheStringToHash(key, number):
	return key + str(number)

def checkForZeros(hashString):
	check = True
	for i in range(5):
		if not hashString[i] == '0':
			check = False
			break
	return check

import hashlib

found = False
number = 1
keyTest1 = 'abcdef'
keyTest2 = 'pqrstuv'
key = 'yzbqklnj'

while not found:
	stringToHash = getTheStringToHash(key, number)
	hashedString = hashlib.md5(stringToHash.encode())
	found = checkForZeros(hashedString.hexdigest())
	number +=1

print(number - 1)

