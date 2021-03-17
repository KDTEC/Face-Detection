# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:57:39 2021

@author: Kshitij
"""

import cv2 as cv

img=cv.imread('group2.jpg')

cv.imshow('Image of group of people',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

harr_cascade = cv.CascadeClassifier('harr_face.xml')

faces_rect = harr_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow('Detected_faces',img)



cv.waitKey(0)
cv.destroyAllWindows()