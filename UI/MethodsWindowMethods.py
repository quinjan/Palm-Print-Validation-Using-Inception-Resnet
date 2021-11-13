# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:01:39 2021

@author: quinj
"""

from PyQt5 import QtCore, QtWidgets
from UI.MethodsWindow import Ui_MethodsWindow
from UI.CaptureWindowMethods import CaptureWindow
from UI.TrainModelWindowMethods import TrainModelWindow
from UI.ValidateUserWindowMethods import ValidateUserWindow
from Common.DatasetGenerator import DatasetGenerator
import sys

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
    
    def flush(self):
        pass

class MethodsWindow(QtWidgets.QDialog, Ui_MethodsWindow):
    
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MethodsWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.captureWindow = CaptureWindow()
        self.trainModelWindow = TrainModelWindow()
        self.validateUserWindow = ValidateUserWindow()
        
        self.captureWindow.clicked.connect(self.ShowMethodsWindow)
        self.trainModelWindow.clicked.connect(self.ShowMethodsWindow)
        self.validateUserWindow.clicked.connect(self.ShowMethodsWindow)
        
        self.method1PushButton.clicked.connect(self.Method1Clicked)
        self.method2PushButton.clicked.connect(self.Method2Clicked)
        self.method3PushButton.clicked.connect(self.Method3Clicked)
        self.backPushButton.clicked.connect(self.clicked)
    
    def ShowUserNameDialog(self):
        self.userName, result = QtWidgets.QInputDialog.getText(self, "Input Username", "Enter Your Name:")
        return result

    def ShowMethodsWindow(self):
        
        try:
            if(sys.stdout != self.oldstdout):
                sys.stdout = self.oldstdout
        except:
            pass
        
        self.captureWindow.close()
        self.trainModelWindow.hide()
        self.validateUserWindow.close()
        self.show()
        
    def Method1Clicked(self):
        if (self.selectedAction == "GenerateDataset"):
            result = self.ShowUserNameDialog()
            if(result):
                self.captureWindow.selectedMethod = DatasetGenerator.Methods.Method1._name_
                self.ShowCaptureWindow()
        elif (self.selectedAction == "TrainModel"):
            self.trainModelWindow.selectedMethod = DatasetGenerator.Methods.Method1._name_
            self.trainModelWindow.windowTitlelabel.setText(self.method1PushButton.text())
            self.ShowTrainModelWindow()
        elif (self.selectedAction == "ValidateUser"):
            result = self.ShowUserNameDialog()
            if(result):
                self.validateUserWindow.selectedMethod = DatasetGenerator.Methods.Method1._name_
                self.validateUserWindow.methodDescriptionLabel.setText(self.method1PushButton.text())
                self.ShowValidateUserWindow()

    def Method2Clicked(self):
        if (self.selectedAction == "GenerateDataset"):
            result = self.ShowUserNameDialog()
            if(result):
                self.captureWindow.selectedMethod = DatasetGenerator.Methods.Method2._name_
                self.ShowCaptureWindow()
        elif (self.selectedAction == "TrainModel"):
            self.trainModelWindow.selectedMethod = DatasetGenerator.Methods.Method2._name_
            self.trainModelWindow.windowTitlelabel.setText(self.method2PushButton.text())
            self.ShowTrainModelWindow()
        elif (self.selectedAction == "ValidateUser"):
            result = self.ShowUserNameDialog()
            if(result):
                self.validateUserWindow.selectedMethod = DatasetGenerator.Methods.Method2._name_
                self.validateUserWindow.methodDescriptionLabel.setText(self.method2PushButton.text())
                self.ShowValidateUserWindow()

            
    def Method3Clicked(self):
        if (self.selectedAction == "GenerateDataset"):
            result = self.ShowUserNameDialog()
            if(result):
                self.captureWindow.selectedMethod = DatasetGenerator.Methods.Method3._name_
                self.ShowCaptureWindow()
        elif (self.selectedAction == "TrainModel"):
            self.trainModelWindow.selectedMethod = DatasetGenerator.Methods.Method3._name_
            self.trainModelWindow.windowTitlelabel.setText(self.method3PushButton.text())
            self.ShowTrainModelWindow()
        elif (self.selectedAction == "ValidateUser"):
            result = self.ShowUserNameDialog()
            if(result):
                self.validateUserWindow.selectedMethod = DatasetGenerator.Methods.Method3._name_
                self.validateUserWindow.methodDescriptionLabel.setText(self.method3PushButton.text())
                self.ShowValidateUserWindow()
            
    def ShowCaptureWindow(self):
        self.oldstdout = sys.stdout
        sys.stdout = EmittingStream(textWritten=self.captureWindow.normalOutputWritten)
        
        self.captureWindow.userName = self.userName
        self.hide()
        self.captureWindow.show()
        self.captureWindow.start_webcam()
    
    def ShowTrainModelWindow(self):
        self.oldstdout = sys.stdout
        sys.stdout = EmittingStream(textWritten=self.trainModelWindow.normalOutputWritten)
        
        self.trainModelWindow.shellOutputTextEdit.clear()
        
        self.hide()
        self.trainModelWindow.show()

    def ShowValidateUserWindow(self):
        self.validateUserWindow.userName = self.userName
        
        self.hide()
        self.validateUserWindow.start_webcam()
        self.validateUserWindow.show()
            
        