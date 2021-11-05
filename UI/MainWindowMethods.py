# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:59:31 2021

@author: quinj
"""

from PyQt5 import QtWidgets
from UI.MainWindow import Ui_MainWindow
from UI.MethodsWindowMethods import MethodsWindow
import enum

class MainWindow(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.methodsWindow = MethodsWindow()
        
        self.methodsWindow.clicked.connect(self.ShowMainWindow)
        
        self.generateDatasetPushButton.clicked.connect(self.GenerateDatasetClicked)
        self.trainModelPushButton.clicked.connect(self.TrainModelClicked)
        self.validateUserPushButton.clicked.connect(self.ValidateUserClicked)
    
    class Actions(enum.Enum):
        GenerateDataset = 1
        TrainModel = 2
        ValidateUser = 3
    
    def GenerateDatasetClicked(self):
        self.methodsWindow.selectedAction = self.Actions.GenerateDataset._name_
        self.ShowMethodsWindow()
    
    def TrainModelClicked(self):
        self.methodsWindow.selectedAction = self.Actions.TrainModel._name_
        self.ShowMethodsWindow()
    
    def ValidateUserClicked(self):
        self.methodsWindow.selectedAction = self.Actions.ValidateUser._name_
        self.ShowMethodsWindow()
    
    def ShowMethodsWindow(self):
        self.hide()
        self.methodsWindow.show()
        
    def ShowMainWindow(self):
        self.methodsWindow.hide()
        self.show()