# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:18:05 2021

@author: quinj
"""
from Common.Helpers.CLAHE import CLAHE
import numpy as np 
import cv2

class Morph():
    def __init__(self):
        print("Morph Class Initialized")
        
    def Process(self, image):
        
        def my_dilation(img, struct):
            out = np.zeros(img.shape, dtype='int')
            H = (struct.shape[0] - 1) // 2
            W = (struct.shape[1] - 1) // 2
            for i in range(H, img.shape[0] - H):
                for j in range(W, img.shape[1] - W):
                    if img[i, j] == 255:
                        for m in range(-H, H + 1):
                            for n in range(-W, W + 1):
                                out[i + m, j + n] = struct[H + m, W + n]
            return out.astype(img.dtype)

        def my_erosion(img, struct):
            out = np.zeros(img.shape, dtype='int')
            H = (struct.shape[0] - 1) // 2
            W = (struct.shape[1] - 1) // 2
            for i in range(H, img.shape[0] - H):
                for j in range(W, img.shape[1] - W):
                    for m, n in gener(H, W):
                        if not struct[H + m, W + n]:
                            continue
                        if struct[H + m, W + n] != img[i + m, j + n]:
                            break
                    else:
                        out[i, j] = 255
            return out.astype(img.dtype)

        def gener(p, q):
            for i in range(-p, p + 1):
                for j in range(-q, q + 1):
                    yield i, j
        
        struct = np.array([[0, 0, 255, 255, 255, 0, 0],
                           [0, 255, 255, 255, 255, 255, 0],
                           [255, 255, 255, 255, 255, 255, 255],
                           [255, 255, 255, 255, 255, 255, 255],
                           [255, 255, 255, 255, 255, 255, 255],
                           [0, 255, 255, 255, 255, 255, 0],
                           [0, 0, 255, 255, 255, 0, 0]]).astype('int')

        img = cv2.medianBlur(image, 5)
        th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
        dilation = my_dilation(th, struct)
        erosion = my_erosion(th, struct)
        edge = np.subtract(dilation, erosion)

        return edge
        