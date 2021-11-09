# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 22:29:35 2021

@author: quinj
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.ValidateUserWindow import Ui_ValidateUserWindow
from Common.MachineLearningModel import MachineLearningModel
from Common.DatasetGenerator import DatasetGenerator
import sys
import os
import cv2
import numpy as np

class ValidatorWorker(QtCore.QThread):
    
    result = QtCore.pyqtSignal(bool)
    
    def __init__(self, selectedMethod, image, userName, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.selectedMethod = selectedMethod
        self.image = image
        self.userName = userName
    
    def run(self):
        self.machineLearning = MachineLearningModel(self.selectedMethod)
        response = self.machineLearning.ValidateImage(self.image, self.userName)
        self.result.emit(response)
    
    def stop(self):
        self.terminate()



class ValidateUserWindow(QtWidgets.QMainWindow, Ui_ValidateUserWindow):
    
    clicked = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(ValidateUserWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.validatorWorker = QtCore.QThread()
        
        self.imageLabel.setScaledContents(True)
        self.capture = None
        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        
        self.returnPushButton.clicked.connect(self.BackButtonClicked)
        self.capturePushButton.clicked.connect(self.capture_image)
        
        self.statusBar().showMessage('Ready')
        
        
    def ValidateUser(self, image):
        # test = cv2.imread('Robert.png')
        self.validatorWorker = ValidatorWorker(self.selectedMethod, image, self.userName)
        self.validatorWorker.result.connect(self.onFinished)
        self.returnPushButton.setEnabled(False)
        self.capturePushButton.setEnabled(False)
        self.validatorWorker.start()
        
    def ShowValidateUserFinishedDialog(self, result):
        self.returnPushButton.setEnabled(True)
        self.capturePushButton.setEnabled(True)
        if(result):
            QtWidgets.QMessageBox.information(self, "Done!", "Validation Done")
        else:
            QtWidgets.QMessageBox.critical(self, "Error!", "Invalid User")
    
    @QtCore.pyqtSlot()
    def capture_image(self):
        flag, frame= self.capture.read()
        if flag:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ds = DatasetGenerator(self.selectedMethod, self.userName)
            image = ds.Preprocessing(self.selectedMethod, frame)
            self.ValidateUser(image)

    def BackButtonClicked(self):
        self.destroy_webcam()
        self.clicked.emit()
    
    @QtCore.pyqtSlot(bool)
    def onFinished(self, result):
        self.validatorWorker.stop()
        self.ShowValidateUserFinishedDialog(result)
            
    @QtCore.pyqtSlot()
    def start_webcam(self):
        print("Initializing Camera")
        if self.capture is None:
            self.capture =cv2.VideoCapture(0 + cv2.CAP_DSHOW)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer.start()
        self.usernameLabel.setText(self.userName)
    
    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image=self.capture.read()
        image = cv2.flip(image, 1)
        self.displayImage(image, True)
    
    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        try:
            if len(img.shape)==3 :
                if img.shape[2]==4:
                    qformat = QtGui.QImage.Format_RGBA8888
                else:
                    qformat = QtGui.QImage.Format_RGB888
            outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
            outImage = outImage.rgbSwapped()
            if window:
                self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))
        except:
            print("Camera Closed")
    
    def destroy_webcam(self):
        self.timer.stop()
        print("Destroying Camera")
        if self.capture != None:
            self.capture.release()
            self.capture = None
