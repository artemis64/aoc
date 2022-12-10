file = open('input10.txt', 'r')

X = 1
pixelLine = ''

for line in file:
	line = line.strip()
	line = line.split()
	if len(line) > 1:
		if len(pixelLine) in [X-1, X, X+1]:
			pixelLine += '#'
		else:
			pixelLine += '.'
		if len(pixelLine) == 40:
			print(pixelLine)
			pixelLine = ''
		if len(pixelLine) in [X-1, X, X+1]:
			pixelLine += '#'
		else:
			pixelLine += '.'
		X += int(line[1])
		if len(pixelLine) == 40:
			print(pixelLine)
			pixelLine = ''
	else:
		if len(pixelLine) in [X-1, X, X+1]:
			pixelLine += '#'
		else:
			pixelLine += '.'
		if len(pixelLine) == 40:
			print(pixelLine)
			pixelLine = ''