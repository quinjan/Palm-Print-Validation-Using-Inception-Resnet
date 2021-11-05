# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:01:39 2021

@author: quinj
"""

from PyQt5 import QtCore, QtWidgets
from UI.MethodsWindow import Ui_MethodsWindow
from UI.CaptureWindowMethods import CaptureWindow


class MethodsWindow(QtWidgets.QDialog, Ui_MethodsWindow):
    
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MethodsWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.captureWindow = CaptureWindow()
        
        self.captureWindow.clicked.connect(self.ShowMethodsWindow)
        
        self.method1PushButton.clicked.connect(self.ShowUserNameDialog)
        self.method2PushButton.clicked.connect(self.ShowUserNameDialog)
        self.method3PushButton.clicked.connect(self.ShowUserNameDialog)
        self.backPushButton.clicked.connect(self.clicked)
    
    def ShowUserNameDialog(self):
        if (self.selectedAction == "GenerateDataset"):
            self.username, result = QtWidgets.QInputDialog.getText(self, "Input Username", "Enter Your Name:")
            if(result):
                self.captureWindow.usernameLabel.setText(self.username)
                self.hide()
                self.captureWindow.show()
                self.captureWindow.start_webcam()
    
    def ShowMethodsWindow(self):
        self.captureWindow.close()
        self.show()
            
        