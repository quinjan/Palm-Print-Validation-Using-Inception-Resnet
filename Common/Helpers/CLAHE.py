# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:26:22 2021

@author: quinj
"""

import cv2
import numpy as np
import math
import time

class CLAHE():
    def __init__(self):
        print("CLAHE Class Initialized")
    
    def Process(self, image):

        bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        lab_planes = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=10)
        
        plane1 = clahe.apply(lab_planes[0])
        plane2 = lab_planes[1]
        plane3 = lab_planes[2]
        
        lst = [plane1, plane2, plane3]
        
        t = tuple(lst)
        
        lab = cv2.merge(t)
        bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

        return gray