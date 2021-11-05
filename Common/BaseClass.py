# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 07:45:29 2021

@author: quinj
"""
from Common.Helpers.CLAHE import CLAHE
from Common.Helpers.ROI import ROI
from Common.Helpers.Morph import Morph
from Common.Helpers.Sobel import Sobel

class BaseClass:
    def __init__(self):
        print("Base Class Initiated")

    def Extract_ROI(self, image):
        print("Extract ROI")
        roi = ROI()
        extracted = roi.Process(image)
        return extracted

    def Preprocessing(self, method, image):
        print("Pre Processing Method")
        if (method == "Method 1"):
            result = self.Method1(image)
        elif (method == "Method 2"):
            result = self.Method2(image)
        elif (method == "Method 3"):
            result = self.Method3(image)
        else:
            raise ValueError("Invalid Method")
        
        return result


    def Method1(self, img):
        clahe = CLAHE()
        processedImage = clahe.Process(img)
        return processedImage
    
    def Method2(self, img):
        morph = Morph()
        processedImage = morph.Process(img)
        return processedImage
    
    def Method3(self, img):
        sobel = Sobel()
        processedImage = sobel.Process(img)
        return processedImage