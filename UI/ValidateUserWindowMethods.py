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
import time

class FrameGrabber(QtCore.QThread):
    def __init__(self, parent=None):
        super(FrameGrabber, self).__init__(parent)

    signal = QtCore.pyqtSignal(np.ndarray)
    
    cameraLoaded = QtCore.pyqtSignal(bool)

    def run(self):
        #Uncomment for RPI
        #os.system('sudo modprobe bcm2835-v4l2')

        self.cap = cv2.VideoCapture("http://raspberrypi:5000/video_feed")
        time.sleep(5)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
        if(self.cap.isOpened()):
            self.ThreadActive = True
            self.cameraLoaded.emit(True)
        
        else:
            self.ThreadActive = False
        
        while self.ThreadActive:
            success, frame = self.cap.read()
            if success:
                self.signal.emit(frame)
        self.cap.release()
        self.quit()
    
    def stop(self):
        self.ThreadActive = False

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
        
class Processor(QtCore.QThread):
    def __init__(self, image, selectedMethod, userName, parent=None):
        super(Processor, self).__init__(parent)
        self.image = image
        self.userName = userName
        self.selectedMethod = selectedMethod
        self.dsGen = DatasetGenerator(selectedMethod , userName)
        self.dsGen.InitializeDatasetFolder()
    
    signal = QtCore.pyqtSignal(np.ndarray)
    
    def run(self):
        print("Processing image: " + self.userName)
        self.preprocessedImage = self.dsGen.Preprocessing(self.selectedMethod, self.image)
        print("Processing image: " + self.userName + "Done.")
        self.signal.emit(self.preprocessedImage)
        
    def stop(self):
        self.terminate()


class ValidateUserWindow(QtWidgets.QMainWindow, Ui_ValidateUserWindow):
    
    clicked = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(ValidateUserWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.validatorWorker = QtCore.QThread()
        self.grabber = QtCore.QThread()
        self.imageProcessor = QtCore.QThread()
        
        self.imageLabel.setScaledContents(True)
        
        self.returnPushButton.clicked.connect(self.BackButtonClicked)
        self.capturePushButton.clicked.connect(self.capture_image)
        
        self.statusBar().showMessage('Ready')
        
        
    def ValidateUser(self, image):
        # test = cv2.imread('Robert.png')
        self.validatorWorker = ValidatorWorker(self.selectedMethod, image, self.userName)
        self.validatorWorker.result.connect(self.onFinished)
        self.validatorWorker.start()
        
    def ShowValidateUserFinishedDialog(self, result):
        self.statusBar().showMessage('Ready')
        self.returnPushButton.setEnabled(True)
        self.capturePushButton.setEnabled(True)
        if(result):
            QtWidgets.QMessageBox.information(self, "Done!", "Validation Done")
        else:
            QtWidgets.QMessageBox.critical(self, "Error!", "Invalid User")
    
    @QtCore.pyqtSlot()
    def capture_image(self):
        QtWidgets.QApplication.beep()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        print("Captured: " + self.userName)
        
        self.imageProcessor = Processor(self.frame, self.selectedMethod, self.userName)
        self.imageProcessor.signal.connect(self.ProcessFinished)
        self.returnPushButton.setEnabled(False)
        self.capturePushButton.setEnabled(False)
        self.statusBar().showMessage('Processing Image')
        self.imageProcessor.start()
        
    @QtCore.pyqtSlot(np.ndarray)
    def ProcessFinished(self, image):
        self.statusBar().showMessage('Validating User')
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
        print("Starting Webcam")
        self.imageLabel.setText("Loading Camera......")
        self.capturePushButton.setEnabled(False)
        
        self.grabber = FrameGrabber()
        self.grabber.cameraLoaded.connect(self.CameraInitialized)
        self.grabber.signal.connect(self.update_frame)
        self.grabber.start()
        
        self.ds = DatasetGenerator(self.selectedMethod, self.userName)
        self.usernameLabel.setText(self.userName)
    
    @QtCore.pyqtSlot(bool)
    def CameraInitialized(self, isCameraInitialized):
        if(isCameraInitialized):
            self.capturePushButton.setEnabled(True)
    
    @QtCore.pyqtSlot(np.ndarray)
    def update_frame(self, frame):
        self.frame = frame
        self.displayImage(self.frame)
    
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
        print("Destroying Camera")
        self.grabber.stop()
