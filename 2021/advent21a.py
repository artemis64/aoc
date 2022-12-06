file = open('input21.txt', 'r')

player1 = file.readline()
player1 = player1.strip()
player1 = player1.split()
player1 = int(player1[4])

player2 = file.readline()
player2 = player2.strip()
player2 = player2.split()
player2 = int(player2[4])

dice = 1
roll = 0
player1score = 0
player2score = 0

while not (player2score >= 1000 or player1score >= 1000):
	for i in range(3):
		player1 +=dice
		dice = 1 if dice + 1 > 100 else dice + 1
		roll +=1
	while player1 > 10:
		player1 -=10
	player1score +=player1
	if player1score >= 1000:
		break
	for i in range(3):
		player2 +=dice
		dice = 1 if dice + 1 > 100 else dice + 1
		roll +=1
	while player2 > 10:
		player2 -=10
	player2score +=player2
total = roll * min(player1score, player2score)
print(roll)
print(min(player1score, player2score))
print(total)
