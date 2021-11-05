# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:12:06 2021

@author: quinj
"""
from Common.BaseClass import BaseClass
import numpy as np
from matplotlib import pyplot as plt
import cv2

def show(img):
    plt.imshow(img, cmap='gray')
    plt.xticks([])
    plt.yticks([])

print("Test ROI")
test = BaseClass()
img_original = cv2.imread('Test Image.jpg', 0)
result = test.Extract_ROI(img_original)

# method1test = test.Preprocessing("Method 1", result)
# method2test = test.Preprocessing("Method 2", result)
method3test = test.Preprocessing("Method 3", result)

# plt.figure(figsize=(5,5))
# show(method1test)

# plt.figure(figsize=(5,5))
# show(method2test)

plt.figure(figsize=(5,5))
show(method3test)
