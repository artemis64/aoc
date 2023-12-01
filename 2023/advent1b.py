file = open('input1.txt', 'r') 
writtenDigits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] # list of written digits

summa = 0                       
for line in file:               
    line = line.strip()         
    digits = []  # in digits list will be stored tuples (pairs) - on the first (0th) position is index of a position the digit starts on and on the second (1st) position is the digit itself

    for i, char in enumerate(line):         # loop through every character in line with keeping the count (i-th loop)  searching for digits in a form of a number
        if char.isdigit():      
            digits.append((i, int(char)))  # i is the position of a digit in the line, int converts the digit from character (string) to integer

    for i, writtenDigit in enumerate(writtenDigits): # loop through all the digits in written for to search for the in the line
        index = 0 # keeping count where do I start the search (I want to add to digits list all occurrences, not just the first one)
        while index < len(line) and index >= 0:  # I search for the specific digit in the line multiple times - the find method always gives me back just the first occurrence 
            if writtenDigit in line[index:]:  # if we find the digit in written form on the line starting on the index-th position or later ...
                digits.append((line[index:].find(writtenDigit) + index, i)) # we append what we found to digits. The position is in respect to the complete line
                index += line[index:].find(writtenDigit) + 1 # next time we want to start searching one character after where the current digit started
            else: 
                index = -1
    digits.sort() #sorts the list by the first (0th) position - the position of the digit in the line
    summa += 10*digits[0][1] + digits[-1][1] # on the place of tenths we use the first digit, units are the last digit because the list was sorted
print(summa)