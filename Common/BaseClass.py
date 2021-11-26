# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 07:45:29 2021

@author: quinj
"""
from Common.Helpers.CLAHE import CLAHE
from Common.Helpers.ROI import ROI
from Common.Helpers.Morph import Morph
from Common.Helpers.Sobel import Sobel
import enum

class BaseClass:
    def __init__(self):
        print("Base Class Initiated")
        
    class Methods(enum.Enum):
        Method1 = 1
        Method2 = 2
        Method3 = 3

    def Extract_ROI(self, image):
        print("Extracting ROI")
        roi = ROI()
        extracted = roi.Process(image)
        return extracted

    def Preprocessing(self, method, image):
        print("Pre Processing Method")
        if (method == self.Methods.Method1._name_):
            result = self.Method1(image)
        elif (method == self.Methods.Method2._name_):
            result = self.Method2(image)
        elif (method == self.Methods.Method3._name_):
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