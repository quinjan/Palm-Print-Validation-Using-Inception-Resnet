# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:01:39 2021

@author: quinj
"""

from PyQt5 import QtCore, QtWidgets
from UI.MethodsWindow import Ui_MethodsWindow
from UI.CaptureWindowMethods import CaptureWindow
from Common.DatasetGenerator import DatasetGenerator


class MethodsWindow(QtWidgets.QDialog, Ui_MethodsWindow):
    
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MethodsWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.captureWindow = CaptureWindow()
        
        self.captureWindow.clicked.connect(self.ShowMethodsWindow)
        
        self.method1PushButton.clicked.connect(self.Method1Clicked)
        self.method2PushButton.clicked.connect(self.Method2Clicked)
        self.method3PushButton.clicked.connect(self.Method3Clicked)
        self.backPushButton.clicked.connect(self.clicked)
    
    def ShowUserNameDialog(self):
        if (self.selectedAction == "GenerateDataset"):
            self.userName, result = QtWidgets.QInputDialog.getText(self, "Input Username", "Enter Your Name:")
            return result
        return False
        
    
    def ShowMethodsWindow(self):
        self.captureWindow.close()
        self.show()
        
    def Method1Clicked(self):
        result = self.ShowUserNameDialog()
        if(result):
            self.captureWindow.selectedMethod = DatasetGenerator.Methods.Method1._name_
            self.ShowCaptureWindow()
    
    def Method2Clicked(self):
        result = self.ShowUserNameDialog()
        if(result):
            self.captureWindow.selectedMethod = DatasetGenerator.Methods.Method2._name_
            self.ShowCaptureWindow()
        
    def Method3Clicked(self):
        result = self.ShowUserNameDialog()
        if(result):
            self.captureWindow.selectedMethod = DatasetGenerator.Methods.Method3._name_
            self.ShowCaptureWindow()
    
    def ShowCaptureWindow(self):
        self.captureWindow.userName = self.userName
        self.hide()
        self.captureWindow.show()
        self.captureWindow.start_webcam()
            
        