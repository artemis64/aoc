def addDarkBorder(image, infinitePixel):
	for row in image:
		row.append(infinitePixel)
		row.insert(0, infinitePixel)
	image.insert(0, [infinitePixel for i in range(len(image[0]))])
	image.append([infinitePixel for i in range(len(image[0]))])
	return image

def countLightPixels(image):
	count = 0
	for row in image:
		for pixel in row:
			count += pixel
	return count

def enhancePicture(image, key):
	newImage = []
	for rowIndex in range(len(image)-2):
		newImage.append([])
		for pixelIndex in range(len(image[rowIndex])-2):
			#print("enhancing square starting with ({}, {})".format(rowIndex,pixelIndex))
			binaryString = ''
			for iRow in range(3):
				for iPixel in range(3):
					binaryString += str(image[rowIndex + iRow][pixelIndex + iPixel])
			newPixel = 0
			if key[int(binaryString,2)] == '#':
				newPixel = 1
			newImage[-1].append(newPixel)
	return newImage



file = open('input20.txt', 'r')
enhencementAlgorithm = file.readline()
enhencementAlgorithm = enhencementAlgorithm.strip()

file.readline()

inputImage = []
for line in file:
	line = line.strip()
	row = []
	for pixel in line:
		if pixel == '.':
			row.append(0)
		else:
			row.append(1)
	inputImage.append(row)
inputImage = addDarkBorder(inputImage, 0)
inputImage = addDarkBorder(inputImage, 0)

for instance in range(50):
	infinityPixelPosition = 0 if inputImage[0][0] == 0 else 511
	inputImage = enhancePicture(inputImage, enhencementAlgorithm)
	if enhencementAlgorithm[infinityPixelPosition] == '.':
		inputImage = addDarkBorder(inputImage, 0)
		inputImage = addDarkBorder(inputImage, 0)	
	else:
		inputImage = addDarkBorder(inputImage, 1)
		inputImage = addDarkBorder(inputImage, 1)

print(countLightPixels(inputImage))




