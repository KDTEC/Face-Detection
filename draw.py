# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:40:18 2021

@author: Kshitij
"""

import cv2 as cv
import numpy as np

# img = cv.imread('walle.jpg')
# cv.imshow('Image',img)

blank_img = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank_img)

# Painting the image certain color

# blank_img[:] = 0,0,255
# cv.imshow('Red',blank_img)

# blank_img[200:300, 300:400] = 0,0,255
# cv.imshow('Red',blank_img)

# Draw a rectangle

cv.rectangle(blank_img, (0,0), (250,250), (0,255,0), thickness=-1)
cv.imshow('Rectangle',blank_img)

# Draw a circle

cv.circle(blank_img, (250,250), 40, (0,0,255), thickness=6)
cv.imshow('Circle',blank_img)

#Draw a line

cv.line(blank_img, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow('Line',blank_img)

#put text in a image

cv.putText(blank_img, 'Hello im kshitij!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text',blank_img)




cv.waitKey(0)
cv.destroyAllWindows()