# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:50:40 2021

@author: Kshitij
"""

import cv2 as cv

img=cv.imread('walle.jpg')

cv.imshow('Image',img)

# Convert to gray scale

gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray_img)

cv.waitKey(0)
cv.destroyAllWindows()
