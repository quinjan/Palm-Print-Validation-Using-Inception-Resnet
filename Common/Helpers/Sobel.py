# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:18:19 2021

@author: quinj
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpig

class Sobel():
    def __init__(self):
        print("Sobel Class Initialized")
    
    def Process(self, image):
        #define horizontal and Vertical sobel kernels
        Gx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
        Gy = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
        
        sob_x = self.convolve(image, Gx) / 8.0
        sob_y = self.convolve(image, Gy) / 8.0
        
        #calculate the gradient magnitude of vectors
        sob_out = np.sqrt(np.power(sob_x, 2) + np.power(sob_y, 2))
        # mapping values from 0 to 255
        sob_out = (sob_out / np.max(sob_out)) * 255
        
        return sob_out
        
    def convolve(self, X, F):
        # height and width of the image
        X_height = X.shape[0]
        X_width = X.shape[1]
        
        # height and width of the filter
        F_height = F.shape[0]
        F_width = F.shape[1]
        
        H = (F_height - 1) // 2
        W = (F_width - 1) // 2
        
        #output numpy matrix with height and width
        out = np.zeros((X_height, X_width))
        #iterate over all the pixel of image X
        for i in np.arange(H, X_height-H):
            for j in np.arange(W, X_width-W):
                sum = 0
                #iterate over the filter
                for k in np.arange(-H, H+1):
                    for l in np.arange(-W, W+1):
                        #get the corresponding value from image and filter
                        a = X[i+k, j+l]
                        w = F[H+k, W+l]
                        sum += (w * a)
                out[i,j] = sum
        #return convolution  
        return out