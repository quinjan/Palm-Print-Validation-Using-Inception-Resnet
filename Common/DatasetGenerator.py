# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:31:42 2021

@author: quinj
"""

from Common.BaseClass import BaseClass
from pathlib import Path
import cv2
import splitfolders
import shutil

class DatasetGenerator(BaseClass):
    def __init__(self, method, username):
        print("DatasetGenerator Class Initiated")
        self.method = method
        self.username = username
        self.sourcePath = "Datasets/{}/Sources".format(self.method)
        self.userSourcePath = self.sourcePath + "/{}".format(self.username)
        self.splitPath = "Datasets/{}/Splits".format(self.method)
    
    def InitializeDatasetFolder(self):
        print("Initializing Dataset Folder")
        Path(self.sourcePath).mkdir(parents=True, exist_ok=True)
        Path(self.userSourcePath).mkdir(parents=True, exist_ok=True)
        Path(self.splitPath).mkdir(parents=True, exist_ok=True)
    
    def StoreImage(self, image, filename):
        preProcessed_Image = self.Preprocessing(self.method, image)
        print("Storing Pre Processed Image {} in".format(filename) + self.userSourcePath)
        cv2.imwrite(self.userSourcePath + "/{}".format(filename), preProcessed_Image)
    
    
    def SplitData(self):
        print("Removing Existing Split Directory")
        shutil.rmtree(self.splitPath)
        print("Splitting Dataset")
        splitfolders.ratio(self.sourcePath, output=self.splitPath, seed=1337, ratio=(.8, .2), group_prefix=None)
        
    def DeleteCurrentUserDataset(self):
        print("Removing {} from Source Directory".format(self.username))
        shutil.rmtree(self.userSourcePath)