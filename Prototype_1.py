################################################################################################################################
#	Name:		Elizabeth Govan
#	Student 	Number: C14307346
#	Course:		DT211C/4
#	StartDate:	01/10/17
#	FinishDate: 
#	
#	Title: Assignment 1 - Master Forgery
#	Introduction: 
#		Placing an image of a signature and insreting it no to a form  
#		preferably use a systematic approach
#		e.g step-by-step
#		1. Open any image;
#		2. Crop out the fourth quadrant of the image;
#		Comment on experiments
#		use references (Harvard Referencing System) - not weblink
#		Comment on performance
# 	
################################################################################################################################
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import rawpy
import imageio

f = easygui.fileopenbox()
frame = cv2.imread(f)

# raw = rawpy.imread(frame)
# rgb = raw.postprocess()

G = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
B3 = cv2.adaptiveThreshold(G, maxValue = 255,
adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
thresholdType = cv2.THRESH_BINARY,
blockSize = 5,C = 11)
B3 = B3 -255
cv2.imwrite("binary.jpg",B3)		
B3,contours,_ = cv2.findContours(B3,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)

# I = cv2.drawContours(frame, contours, contourIdx=-1,color=(0,255,0), thickness=5)	

areas = [cv2.contourArea(contour) for contour in contours]
maxIndex = np.argmax(areas)
largestContour = contours[maxIndex]

# I = cv2.drawContours(frame, largestContour, contourIdx=-1,color=(0,255,0), thickness=5)	
ellipse = cv2.fitEllipse(largestContour)
cv2.ellipse(frame,ellipse, color=(0,255,0))

cv2.imshow("frame",frame)
cv2.imshow("binary",B3)
cv2.imwrite("final.jpg",frame)
# cv2.imshow("i",I)
key = cv2.waitKey(0)
