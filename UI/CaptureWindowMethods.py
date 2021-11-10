# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:39:41 2021

@author: quinj
"""

import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.CaptureWindow import Ui_CaptureWindow
from Common.DatasetGenerator import DatasetGenerator

class FrameGrabber(QtCore.QThread):
    def __init__(self, parent=None):
        super(FrameGrabber, self).__init__(parent)

    signal = QtCore.pyqtSignal(np.ndarray)
    
    cameraLoaded = QtCore.pyqtSignal(bool)

    def run(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.cameraLoaded.emit(True)
        while self.cap.isOpened():
            success, frame = self.cap.read()
            if success:
                self.signal.emit(frame)
    
    def stop(self):
        self.cap.release()
        self.terminate()
                
# class Processor(QtCore.QThread):
#     def __init__(self, parent=None):
#         super(Processor, self).__init__(parent)
        

class CaptureWindow(QtWidgets.QMainWindow, Ui_CaptureWindow):
    
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CaptureWindow, self).__init__(parent)
        self.setupUi(self)

        self.grabber = QtCore.QThread()
        
        self.statusBar().showMessage('Ready')
        self.returnPushButton.clicked.connect(self.ReturnClicked)
        self.capturePushButton.clicked.connect(self.capture_image)
        
        self.imageLabel.setScaledContents(True)
        self._image_counter = 0
    
    def start_webcam(self):
        print("Starting Webcam")
        self.imageLabel.setText("Loading Camera......")
        self.capturePushButton.setEnabled(False)
        self.processPushButton.setEnabled(False)
        
        self.grabber = FrameGrabber()
        self.grabber.cameraLoaded.connect(self.CameraInitialized)
        self.grabber.signal.connect(self.update_frame)
        self.grabber.start()
        
        self.dsGen = DatasetGenerator(self.selectedMethod , self.userName)
        self.dsGen.InitializeDatasetFolder()
        self.usernameLabel.setText(self.userName + " " + str(self._image_counter))
    
    @QtCore.pyqtSlot(bool)
    def CameraInitialized(self, isCameraInitialized):
        if(isCameraInitialized):
            self.capturePushButton.setEnabled(True)
            self.processPushButton.setEnabled(True)

    def destroy_webcam(self):
        print("Destroying Camera")
        self.grabber.stop()

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

    @QtCore.pyqtSlot()
    def capture_image(self):
        QtWidgets.QApplication.beep()
        name = "{}.png".format(self._image_counter)
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.statusBar().showMessage('Processing Image')
        self.dsGen.StoreImage(self.frame, name)
        self._image_counter += 1
        self.usernameLabel.setText(self.userName + " " + str(self._image_counter))
        self.statusBar().showMessage('Ready')
        
    def ReturnClicked(self):
        self.destroy_webcam()
        self.clicked.emit()
        
        
        
        
        
        