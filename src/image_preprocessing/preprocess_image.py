import cv2
import numpy as np


def remove_lines(document):
	""" This function takes a lined document and removes all horizontal page lines.
	The same document without lines (as if it were blank) is returned.
	"""
	
	temp_document = cv2.cvtColor(document, cv2.COLOR_BGR2GRAY)
	img = cv2.bitwise_not(temp_document)

	th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)

	#step0: identify kernel mask of horizontal lines
	horizontal = th2
	rows,cols = horizontal.shape

	horizontalsize = int(cols / 15)
	horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,3))
	horizontal = cv2.erode(horizontal, horizontalStructure)
	horizontal = cv2.dilate(horizontal, horizontalStructure)
	
	kernel = np.ones((5,5), dtype = "uint8") #strengthen lines so everything is cut out (without residues)
	horizontal = cv2.dilate(horizontal, kernel)

	#step1: identify line edges
	edges = cv2.adaptiveThreshold(horizontal,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,-2)

	#step2: strengthen line size
	kernel = np.ones((2, 2), dtype = "uint8")
	dilated = cv2.dilate(edges, kernel)

	# step3: blur original horiz. lines
	smooth = horizontal.copy()
	smooth = cv2.blur(smooth, (20,20))

	#step4: remove fog around original lines 
	(rows, cols) = np.where(img == 255)
	horizontal[rows, cols] = smooth[rows, cols]

	#step5: subtract line mask from document 
	threshold= set(range(80,256))
	for i, array in enumerate(horizontal):
		for j, element in enumerate(array):
			if element in threshold:
				temp_document[i, j] = 255

	return temp_document