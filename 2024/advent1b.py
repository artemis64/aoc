file = open('input1.txt', 'r')  

summa = 0  
list1 = []
list2 = []                     
for line in file:               
    line = line.strip()
    line = line.split()  
    list1.append(int(line[0]))  
    list2.append(int(line[1]))  
for i in range(len(list1)):
    summa += list1[i] * list2.count(list1[i])
print(summa)