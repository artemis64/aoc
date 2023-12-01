file = open('input1.txt', 'r')  #opens the input file

summa = 0                       #in this variable I will get the final addition
for line in file:               #loop through every line in the input file
    line = line.strip()         #get rid of all the spaces and unvisible characters
    digits = []                 #I will store all the digits in the line in this list
    for char in line:           #loop through every character in the line
        if char.isdigit():      #check if the character is a digit
            digits.append(char) #append it to the digits list if it is

    summa += int(digits[0] + digits[-1]) #take first (0th) and last (-1st) digit in the list, put them together and the final string convert to integer and add it to our final addition
print(summa)