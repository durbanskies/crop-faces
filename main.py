from random import randint
import cv2
import sys
import os
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import tkinter

tkinter.Tk().withdraw()
filename = askopenfilename()

raw_haar="facehaar.xml" #haar cascade
cascade=cv2.CascadeClassifier(raw_haar)

def croper(path):
	image=cv2.imread(path) #read
	grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #faster

	faces = cascade.detectMultiScale(grey_image,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0) #img,scale,neighbors,size,flags(no)

	for x,y,w,h in faces:
		crop=image[y-10:y+h+10,x-10:x+w+10]#bounding
		os.chdir("faces_extract")
		cv2.imwrite(str(randint(10000,99999))+"-face"+".jpg",crop)
		os.chdir("../")#cd ..
	
if not "faces_extract" in os.listdir("."): #check
	os.mkdir("faces_extract")

croper(filename)
messagebox.showinfo("Done","All extracted faces have been placed in faces_extract folders")
