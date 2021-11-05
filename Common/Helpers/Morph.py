# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:18:05 2021

@author: quinj
"""

from im2dhisteq import im2dhisteq
import numpy as np 
import cv2

class Morph():
    def __init__(self):
        print("Morph Class Initialized")
        
    def Process(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        img = self.Histogram(image)
        kernel = np.ones((5,5),np.uint8)
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        return closing
        
    def Histogram(self, image):
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image_v = image_hsv[:, :, 2].copy()
        
        image_v_2dheq = im2dhisteq(image_v)
        
        image_hsv[:, :, 2] = image_v_2dheq.copy()
        image_2dheq = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
             
        return image_2dheq
        