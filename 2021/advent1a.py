file = open('input1.txt', 'r')
count = 0

previousNumber = int(file.readline().strip())
print("{} {}".format(previousNumber, "N/A"))

while True:

    number = file.readline().strip()

    if not number:
        break
    number = int(number)
    string = "decreased"

    if number > previousNumber:
        count += 1
        string = "increased"
    #print("{} {}".format(number, string))
    previousNumber = number


    
print("In total increased {} times".format(count))
 
file.close()